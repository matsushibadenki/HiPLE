# path: ./agents/generator_agent.py
# title: GeneratorAgent with Execution Strategy
# description: エキスパートの実行戦略に応じて、インライン実行とワーカー実行を切り替える。

import os
import uuid
import traceback
from typing import List, Dict, Any, cast, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import SubTask, ExpertModel, Milestone
from services.model_loader import ModelLoaderService # 修正
from services.worker_manager import WorkerManagerService, WorkerExecutionError # 修正
from agents.base_agent import BaseAgent
from diffusers import DiffusionPipeline

class GeneratorAgent(BaseAgent):
    """
    エキスパートの実行戦略に応じてタスクを実行するエージェント (HiPLE-G)
    """
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    def __init__(self, model_loader: ModelLoaderService, worker_manager: WorkerManagerService):
        super().__init__(model_loader)
        self.worker_manager = worker_manager
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def execute(self, task: SubTask, expert: ExpertModel, context: Dict[str, Any]) -> str:
        
        if expert.chat_format == "diffusion":
            return self._generate_image(expert, task.description)
        
        messages = self._build_messages_with_context(task, expert, context)

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        try:
            if expert.execution_strategy == "worker":
                print(f"🔩 ワーカープロセス経由で '{expert.name}' を実行します。")
                response_data = self.worker_manager.invoke_llm_worker(expert, messages)
                
                if (
                    "choices" in response_data and response_data["choices"] and
                    "message" in response_data["choices"][0] and
                    "content" in response_data["choices"][0]["message"]
                ):
                    return response_data["choices"][0]["message"]["content"].strip()
                else:
                    raise WorkerExecutionError(f"ワーカーからの応答形式が不正です: {response_data}")
            else:
                # デフォルトはインライン実行
                return self._query_llm(expert, messages)
        except WorkerExecutionError as e:
            print(f"❌ ワーカーの実行に失敗しました: {e}")
            return f"エキスパート '{expert.name}' の実行中にエラーが発生しました。"
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def _build_messages_with_context(self, task: SubTask, expert: ExpertModel, context: Dict[str, Any]) -> List[ChatCompletionRequestMessage]:
        milestone: Optional[Milestone] = context.get('milestone')
        
        if milestone and milestone.title == "Direct Task":
            return [
                {"role": "system", "content": expert.system_prompt},
                {"role": "user", "content": task.description}
            ]
        
        user_prompt = f"""# 全体目標 (L1)\n{context.get('overall_goal')} ...""" # 省略
        # ... (既存のプロンプト構築ロジックは変更なし)
        
        return [
            {"role": "system", "content": expert.system_prompt},
            {"role": "user", "content": user_prompt}
        ]

    def _generate_image(self, expert: ExpertModel, prompt: str) -> str:
        # ... (変更なし)
        return ""