# path: ./agents/generator_agent.py
# title: GeneratorAgent with Self-Evaluation Handling
# description: エキスパートの応答と自己評価を受け取り、タスクオブジェクトに記録する。

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
        
        if expert.chat_format == "diffusion":
            result = self._generate_image(expert, task.description)
            task.self_evaluation = {"confidence": 0.9, "reasoning": "Image generated."}
            return {"status": "completed", "result": result}
        
        consultation_feedback = ""
        if task.consultation_experts:
            consultation_result = self.consultant_agent.execute(
                original_task=task,
                primary_expert=expert,
                all_experts=all_experts
            )
            consultation_feedback = consultation_result.get("response", "")
        
        messages = self._build_messages_with_context(task, expert, context, consultation_feedback)
        
        response_data: Dict[str, Any] = {}
        try:
            if expert.execution_strategy == "worker":
                response_dict_from_worker = self.worker_manager.invoke_llm_worker(expert, messages)
                raw_response_str = response_dict_from_worker.get("choices", [{}])[0].get("message", {}).get("content", "")
                # ワーカーからの応答を自己評価形式にパースする試み
                try:
                    parsed_data = self._parse_self_evaluation_from_str(raw_response_str)
                    response_data = parsed_data
                except (json.JSONDecodeError, KeyError):
                    response_data = {"response": raw_response_str, "self_evaluation": {"confidence": 0.75, "reasoning": "Evaluation from worker could not be parsed."}}
            else:
                response_data = self._query_llm(expert, messages)
        except WorkerExecutionError as e:
            print(f"❌ ワーカーの実行に失敗しました: {e}")
            return {"status": "failed", "result": f"エキスパート '{expert.name}' の実行中にエラーが発生しました。"}

        raw_response = response_data.get("response", "")
        task.self_evaluation = response_data.get("self_evaluation")
        
        tool_use_match = re.search(r'"tool_use"\s*:', raw_response)
        if tool_use_match:
            try:
                # ツール利用要求が自己評価JSONの一部として返される場合
                tool_data = json.loads(raw_response)
                tool_info = tool_data.get("tool_use", {})
                tool_name = tool_info.get("tool_name")
                tool_query = tool_info.get("tool_query")
                tool_url = tool_info.get("tool_url")

                if tool_name and tool_query:
                    print(f"🛠️ ツール利用要求を検知: {tool_name}('{tool_query}')")
                    return {
                        "status": "tool_request",
                        "tool_name": tool_name,
                        "tool_query": tool_query,
                        "tool_url": tool_url
                    }
            except json.JSONDecodeError:
                pass 

        return {"status": "completed", "result": raw_response.strip()}

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

# あなたのタスク (L3)
以上の全てのコンテキスト情報を踏まえ、以下のタスクを実行してください。
**もしタスク実行に外部の情報が必要だと判断した場合、ツール利用を要求するJSONを出力してください。**
あなたの応答は、最終的に自己評価JSONに含める形で出力されます。

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
