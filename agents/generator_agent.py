# path: ./agents/generator_agent.py
# title: GeneratorAgent with Self-Correction, Tool-Use, and Debug Logging
# description: エキスパートの応答と自己評価を受け取り、タスクオブジェクトに記録する。また、自律的にツール利用を判断し要求する。デバッグ用のログ出力機能を含む。

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
    エキスパートの実行戦略に応じてタスクを実行し、自己評価を記録するエージェント (HiPLE-G)
    """
    def __init__(self, model_loader: ModelLoaderService, worker_manager: WorkerManagerService, consultant_agent: ConsultantAgent):
        super().__init__(model_loader)
        self.worker_manager = worker_manager
        self.consultant_agent = consultant_agent

    def execute(self, task: SubTask, expert: ExpertModel, context: Dict[str, Any], all_experts: List[ExpertModel]) -> Dict[str, Any]:
        
        # Step 1: Plannerからの明示的なツール利用指示をチェック
        tool_match = re.search(r"ツール\s*`([^`]+)`\s*を使って「([^」]+)」", task.description)
        if tool_match:
            tool_name = tool_match.group(1).strip()
            tool_query = tool_match.group(2).strip()
            print(f"🛠️ 計画からの明示的なツール利用要求を検知: {tool_name}('{tool_query}')")
            return {
                "status": "tool_request",
                "tool_name": tool_name,
                "tool_query": tool_query,
                "tool_url": None 
            }

        # Step 2: Handle image generation if it's a diffusion model
        if expert.chat_format == "diffusion":
            result = self._generate_image(expert, task.description)
            task.self_evaluation = {"confidence": 0.9, "reasoning": "Image generated."}
            return {"status": "completed", "result": result}
        
        # Step 3: Handle normal text generation tasks
        consultation_feedback = ""
        if task.consultation_experts:
            consultation_result = self.consultant_agent.execute(
                original_task=task,
                primary_expert=expert,
                all_experts=all_experts
            )
            consultation_feedback = consultation_result.get("response", "")
        
        messages = self._build_messages_with_context(task, expert, context, consultation_feedback)
        
        print(f"\n[GeneratorAgent] 📝 LLMに送信するメッセージ (担当: {expert.name}):")
        for i, msg in enumerate(messages):
            print(f"  - Message {i+1} Role: {msg['role']}")
            content_preview = str(msg['content']).replace('\n', ' ').strip()
            print(f"    Content (Preview): {content_preview[:400]}...")

        response_data: Dict[str, Any] = {}
        try:
            if expert.execution_strategy == "worker":
                response_dict_from_worker = self.worker_manager.invoke_llm_worker(expert, messages)
                raw_response_str = response_dict_from_worker.get("choices", [{}])[0].get("message", {}).get("content", "")
                print(f"\n[GeneratorAgent] 🤖 Worker LLMからの生応答 (担当: {expert.name}):\n---\n{raw_response_str}\n---")
                try:
                    parsed_data = self._parse_self_evaluation_from_str(raw_response_str)
                    response_data = parsed_data
                except (json.JSONDecodeError, KeyError):
                    response_data = {"response": raw_response_str, "self_evaluation": {"confidence": 0.75, "reasoning": "Evaluation from worker could not be parsed."}}
            else:
                response_data = self._query_llm(expert, messages)
                print(f"\n[GeneratorAgent] 🤖 LLMからの生応答 (担当: {expert.name}):\n---\n{response_data}\n---")
        except WorkerExecutionError as e:
            print(f"❌ ワーカーの実行に失敗しました: {e}")
            return {"status": "failed", "result": f"エキスパート '{expert.name}' の実行中にエラーが発生しました。"}

        raw_response = response_data.get("response", "")
        task.self_evaluation = response_data.get("self_evaluation")

        if isinstance(raw_response, dict) and "tool_use" in raw_response:
            tool_info = raw_response["tool_use"]
            if isinstance(tool_info, dict) and "tool_name" in tool_info and "tool_query" in tool_info:
                print(f"🛠️ ツール利用要求を検知: {tool_info['tool_name']}('{tool_info['tool_query']}')")
                return {
                    "status": "tool_request",
                    "tool_name": tool_info["tool_name"],
                    "tool_query": tool_info["tool_query"],
                    "tool_url": tool_info.get("tool_url")
                }

        result_str = str(raw_response) if isinstance(raw_response, dict) else raw_response
        return {"status": "completed", "result": result_str.strip()}

    def _parse_self_evaluation_from_str(self, raw_str: str) -> Dict[str, Any]:
        """ 文字列から自己評価JSONをパースする """
        json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_str, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            start_index = raw_str.find('{')
            end_index = raw_str.rfind('}')
            if start_index != -1 and end_index != -1:
                json_str = raw_str[start_index:end_index + 1]
            else:
                raise json.JSONDecodeError("No JSON object found", raw_str, 0)
        
        data = json.loads(json_str)
        if "response" not in data or "self_evaluation" not in data:
            raise KeyError("Missing 'response' or 'self_evaluation' key")
        return data

    def _build_messages_with_context(
        self,
        task: SubTask,
        expert: ExpertModel,
        context: Dict[str, Any],
        consultation_feedback: str = ""
    ) -> List[ChatCompletionRequestMessage]:
        
        milestone: Optional[Milestone] = context.get('milestone')
        system_prompt = expert.system_prompt
        dependency_results = context.get("dependency_results", "")
        rag_results_list = context.get("rag_results", [])
        rag_results_str = "\n".join([f"- {r}" for r in rag_results_list])
        ssv_description = context.get('ssv_description', task.description)
        tool_results = context.get("tool_results", "")
        feedback = task.feedback_history[-1].get("feedback") if task.feedback_history else ""

        if tool_results:
            main_instruction = """# あなたのタスク (L3)
先行タスクによって、以下の「ツールからの情報」が収集されました。
この情報を基に、以下のタスク詳細を達成するための応答を生成してください。
"""
        else:
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            main_instruction = r"""# あなたのタスク (L3)
以上の全てのコンテキスト情報を踏まえ、以下のタスクを実行してください。

**【最重要】**
**もし、このタスクを達成するために外部情報（Web検索やWikipedia）が必要だと判断した場合**、他の応答は一切せず、必ず以下のJSON形式のみを出力してください。

```json
{
  "response": {
    "tool_use": {
      "tool_name": "（'web_search'または'wikipedia_search'）",
      "tool_query": "（検索や実行のための最も具体的で効果的なキーワードや質問）"
    }
  },
  "self_evaluation": {
    "confidence": 1.0,
    "reasoning": "This task requires external information that can be obtained by using a tool."
  }
}
```
**ツールが不要な場合にのみ**、通常の応答と自己評価を生成してください。
"""
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
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

#【重要】前回のレビューからのフィードバック
{feedback if feedback else "フィードバックはありません。"}

{main_instruction}

## タスクの核心 (SSV)
**このタスクで最も重要な目的は「{ssv_description}」を達成することです。**

## タスクの詳細
{task.description}
"""
        
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

    def _generate_image(self, expert: ExpertModel, prompt: str) -> str:
        print(f"🎨 拡散モデル '{expert.name}' を使用して画像を生成します...")
        try:
            pipe = cast(DiffusionPipeline, self.model_loader.load_expert(expert))
            image = pipe(prompt=prompt).images[0]
            
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
