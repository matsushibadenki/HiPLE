# path: ./agents/generator_agent.py
# title: GeneratorAgent with Execution Strategy and Image Generation
# description: エキスパートの実行戦略に応じてタスクを実行するエージェント。画像生成機能を完全に実装。

import os
import uuid
import traceback
from typing import List, Dict, Any, cast, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import SubTask, ExpertModel, Milestone
from services.model_loader import ModelLoaderService
from services.worker_manager import WorkerManagerService, WorkerExecutionError
from agents.base_agent import BaseAgent
from diffusers import DiffusionPipeline

class GeneratorAgent(BaseAgent):
    """
    エキスパートの実行戦略に応じてタスクを実行するエージェント (HiPLE-G)
    """
    def __init__(self, model_loader: ModelLoaderService, worker_manager: WorkerManagerService):
        super().__init__(model_loader)
        self.worker_manager = worker_manager

    def execute(self, task: SubTask, expert: ExpertModel, context: Dict[str, Any]) -> str:
        
        if expert.chat_format == "diffusion":
            return self._generate_image(expert, task.description)
        
        messages = self._build_messages_with_context(task, expert, context)

        try:
            if expert.execution_strategy == "worker":
                print(f"🔩 ワーカープロセス経由で '{expert.name}' を実行します。")
                response_data = self.worker_manager.invoke_llm_worker(expert, messages)
                
                if (
                    "choices" in response_data and response_data["choices"] and
                    "message" in response_data["choices"][0] and
                    "content" in response_data["choices"][0]["message"]
                ):
                    content = response_data["choices"][0]["message"]["content"]
                    return content.strip() if content else ""
                else:
                    raise WorkerExecutionError(f"ワーカーからの応答形式が不正です: {response_data}")
            else:
                # デフォルトはインライン実行
                return self._query_llm(expert, messages)
        except WorkerExecutionError as e:
            print(f"❌ ワーカーの実行に失敗しました: {e}")
            return f"エキスパート '{expert.name}' の実行中にエラーが発生しました。"

    def _build_messages_with_context(self, task: SubTask, expert: ExpertModel, context: Dict[str, Any]) -> List[ChatCompletionRequestMessage]:
        milestone: Optional[Milestone] = context.get('milestone')
        
        if milestone and milestone.title == "Direct Task":
            return [
                {"role": "system", "content": expert.system_prompt},
                {"role": "user", "content": task.description}
            ]
        
        dependency_results = context.get("dependency_results", "")
        rag_results_list = context.get("rag_results", [])
        rag_results_str = "\n".join([f"- {r.get('content', '')}" for r in rag_results_list])

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

# あなたのタスク (L3)
以上の全てのコンテキストを踏まえ、以下のタスクを実行してください。

## タスクの核心 (SSV)
**このタスクで最も重要な目的は「{ssv_description}」を達成することです。**

## タスクの詳細
{task.description}

---
上記の核心（SSV）を最優先し、詳細情報を参考にしながら、具体的で質の高い成果物を生成してください。
"""
        
        return [
            {"role": "system", "content": expert.system_prompt},
            {"role": "user", "content": user_prompt}
        ]

    def _generate_image(self, expert: ExpertModel, prompt: str) -> str:
        """
        拡散モデルを使用して画像を生成し、ファイルパスを文字列として返す。
        """
        print(f"🎨 拡散モデル '{expert.name}' を使用して画像を生成します...")
        try:
            # model_loaderを使用して、設定に基づき拡散モデルのパイプラインをロード
            pipe = cast(DiffusionPipeline, self.model_loader.load_expert(expert))
            
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            # 画像を生成
            # mypyがDiffusionPipelineが呼び出し可能でないと誤認するため、型チェックを無視
            image = pipe(prompt=prompt).images[0] # type: ignore[operator]
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            
            # 出力ディレクトリを作成
            output_dir = "output/images"
            os.makedirs(output_dir, exist_ok=True)
            
            # ユニークなファイル名を生成して保存
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
