# path: ./agents/generator_agent.py
# title: GeneratorAgent with Tool Handling
# description: エキスパートの応答を解析し、ツール利用要求を検知してオーケストレーターに処理を委譲する。

import os
import uuid
import traceback
import json
import re
from typing import List, Dict, Any, cast, Optional, Union
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import SubTask, ExpertModel, Milestone
from services.model_loader import ModelLoaderService
from services.worker_manager import WorkerManagerService, WorkerExecutionError
from agents.base_agent import BaseAgent
from agents.consultant_agent import ConsultantAgent
from diffusers import DiffusionPipeline

class GeneratorAgent(BaseAgent):
    """
    エキスパートの実行戦略に応じてタスクを実行するエージェント (HiPLE-G)
    ツール利用要求を検知し、オーケストレーターに処理を委譲する。
    """
    def __init__(self, model_loader: ModelLoaderService, worker_manager: WorkerManagerService, consultant_agent: ConsultantAgent):
        super().__init__(model_loader)
        self.worker_manager = worker_manager
        self.consultant_agent = consultant_agent

    def execute(self, task: SubTask, expert: ExpertModel, context: Dict[str, Any], all_experts: List[ExpertModel]) -> Dict[str, Any]:
        
        if expert.chat_format == "diffusion":
            result = self._generate_image(expert, task.description)
            return {"status": "completed", "result": result}
        
        consultation_feedback = ""
        if task.consultation_experts:
            consultation_feedback = self.consultant_agent.execute(
                original_task=task,
                primary_expert=expert,
                all_experts=all_experts
            )
        
        messages = self._build_messages_with_context(task, expert, context, consultation_feedback)
        
        raw_response = ""
        try:
            if expert.execution_strategy == "worker":
                response_data = self.worker_manager.invoke_llm_worker(expert, messages)
                if ("choices" in response_data and response_data["choices"] and
                    "message" in response_data["choices"][0] and
                    "content" in response_data["choices"][0]["message"]):
                    raw_response = response_data["choices"][0]["message"]["content"] or ""
                else:
                    raise WorkerExecutionError(f"ワーカーからの応答形式が不正です: {response_data}")
            else:
                raw_response = self._query_llm(expert, messages)
        except WorkerExecutionError as e:
            print(f"❌ ワーカーの実行に失敗しました: {e}")
            return {"status": "failed", "result": f"エキスパート '{expert.name}' の実行中にエラーが発生しました。"}

        tool_use_match = re.search(r'```json\s*(\{[\s\S]*?"tool_use"[\s\S]*?\})\s*```', raw_response, re.DOTALL)
        if tool_use_match:
            try:
                tool_request = json.loads(tool_use_match.group(1))
                tool_info = tool_request.get("tool_use", {})
                tool_name = tool_info.get("tool_name")
                tool_query = tool_info.get("tool_query")
                tool_url = tool_info.get("tool_url")

                if tool_name and tool_query:
                    print(f" টুল利用要求を検知: {tool_name}('{tool_query}')")
                    return {
                        "status": "tool_request",
                        "tool_name": tool_name,
                        "tool_query": tool_query,
                        "tool_url": tool_url
                    }
            except json.JSONDecodeError:
                pass 

        return {"status": "completed", "result": raw_response.strip()}

    def _build_messages_with_context(
        self,
        task: SubTask,
        expert: ExpertModel,
        context: Dict[str, Any],
        consultation_feedback: str = ""
    ) -> List[ChatCompletionRequestMessage]:
        milestone: Optional[Milestone] = context.get('milestone')
        
        tool_results = context.get("tool_results", "")
        system_prompt = self._add_tool_use_prompt_to_system(expert.system_prompt)

        dependency_results = context.get("dependency_results", "")
        rag_results_list = context.get("rag_results", [])
        rag_results_str = "\n".join([f"- {r}" for r in rag_results_list])
        ssv_description = context.get('ssv_description', task.description)

        user_prompt = f"""# 全体目標 (L1)
{context.get('overall_goal', 'N/A')}

# 現在のマイルストーン (L2)
タイトル: {milestone.title if milestone else 'N/A'}
説明: {milestone.description if milestone else 'N/A'}

# 先行タスクからのコンテキスト
{dependency_results if dependency_results else "先行タスクはありません。"}

# 関連情報 (RAG)
{rag_results_str if rag_results_str else "関連情報はありません。"}

# ツールからの情報
{tool_results if tool_results else "ツールからの情報はありません。"}

# 専門家からの助言 (コンサルテーション)
{consultation_feedback if consultation_feedback else "特になし。"}

# あなたのタスク (L3)
以上の全てのコンテキストと専門家の助言を踏まえ、以下のタスクを実行してください。
**もしタスク実行に外部の情報が必要だと判断した場合、後述のJSON形式でツール利用を要求してください。**

## タスクの核心 (SSV)
**このタスクで最も重要な目的は「{ssv_description}」を達成することです。**

## タスクの詳細
{task.description}
"""
        
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

    def _add_tool_use_prompt_to_system(self, original_prompt: str) -> str:
        tool_prompt = """
# ツール利用
タスクの実行に外部情報（例: 最新のニュース、普遍的な知識）が必要な場合は、通常の応答の代わりに、以下のJSON形式のみを出力してください。

```json
{
  "tool_use": {
    "tool_name": "（'wikipedia_search' または 'web_search'）",
    "tool_query": "（ツールで検索・要約させたい具体的な質問文やキーワード）",
    "tool_url": "（web_searchの場合にアクセスしてほしいURL。不要な場合はnull）",
    "reasoning": "（なぜこのツールが必要なのかの簡単な説明）"
  }
}
```
"""
        return original_prompt + "\n" + tool_prompt

    def _generate_image(self, expert: ExpertModel, prompt: str) -> str:
        print(f"🎨 拡散モデル '{expert.name}' を使用して画像を生成します...")
        try:
            pipe = cast(DiffusionPipeline, self.model_loader.load_expert(expert))
            image = pipe(prompt=prompt).images[0]  # type: ignore[operator]
            
            output_dir = "output/images"
            os.makedirs(output_dir, exist_ok=True)
            
            filename = f"{uuid.uuid4()}.png"
            output_path = os.path.join(output_dir, filename)
            image.save(output_path)
            
            absolute_path = os.path.abspath(output_path)
            print(f"🖼️ 画像を保存しました: {absolute_path}")
            return f"画像を {absolute_path} に生成しました。"

        except Exception as e:
            error_message = f"エラー: 画像の生成に失敗しました - {e}"
            print(f"❌ {error_message}")
            traceback.print_exc()
            return error_message

