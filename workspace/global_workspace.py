# /hybrid_llm_system/workspace/global_workspace.py
# グローバル・ワークスペース：思考の履歴と状態を管理

import copy
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage

class GlobalWorkspace:
    """
    エキスパート間の思考プロセスと履歴を共有・管理するグローバル・ワークスペース
    """
    def __init__(self) -> None:
        self.original_prompt: str = ""
        self.thought_process: List[Dict[str, Any]] = []
        self.final_answer: Optional[str] = None
        self.chat_histories: Dict[str, List[ChatCompletionRequestMessage]] = {}

    def initialize(self, expert_names: List[str], system_prompts: Dict[str, str]) -> None:
        """ワークスペースを初期化する"""
        self.original_prompt = ""
        self.thought_process = []
        self.final_answer = None
        for name in expert_names:
            self.chat_histories[name] = [{"role": "system", "content": system_prompts.get(name, "")}]

    def set_initial_prompt(self, prompt: str) -> None:
        """ユーザーからの最初のプロンプトを設定する"""
        self.original_prompt = prompt
        self.add_thought("user", "initial_prompt", prompt)
    
    def add_thought(self, source: str, thought_type: str, content: Any) -> None:
        """思考プロセスに新しいステップを追加する"""
        self.thought_process.append({
            "source": source,       # "user", "orchestrator", "expert:jamba", etc.
            "type": thought_type,   # "initial_prompt", "plan", "expert_query", "expert_response"
            "content": content
        })

    def get_last_thought(self) -> Optional[Dict[str, Any]]:
        """最後の思考ステップを取得する"""
        return self.thought_process[-1] if self.thought_process else None

    def get_full_history_for_expert(self, expert_name: str) -> List[ChatCompletionRequestMessage]:
        """特定のエキスパートの完全な会話履歴を取得する"""
        return copy.deepcopy(self.chat_histories.get(expert_name, []))

    def update_expert_history(self, expert_name: str, user_content: str, assistant_content: str) -> None:
        """特定のエキスパートの会話履歴を更新する"""
        if expert_name in self.chat_histories:
            self.chat_histories[expert_name].append({"role": "user", "content": user_content})
            self.chat_histories[expert_name].append({"role": "assistant", "content": assistant_content})

    def set_final_answer(self, answer: str) -> None:
        """最終的な回答を設定する"""
        self.final_answer = answer
        self.add_thought("orchestrator", "final_answer", answer)