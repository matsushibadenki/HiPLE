# path: ./agents/base_agent.py
# title: Finalized Base Agent (Cleaned)
# description: 応答を確実にハンドリングする最終版の基底クラス。

from abc import ABC, abstractmethod
from typing import List, Any, Optional, cast
from llama_cpp import Llama
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from services.model_loader import ModelLoaderService

class BaseAgent(ABC):
    """
    すべてのエージェントの基本となる抽象基底クラス
    """
    def __init__(self, model_loader: ModelLoaderService):
        self.model_loader = model_loader

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """エージェントの主処理を実行するメソッド"""
        pass

    def _query_llm(self, expert: ExpertModel, messages: List[ChatCompletionRequestMessage]) -> str:
        """LLMに問い合わせを実行する共通メソッド"""
        llm = cast(Llama, self.model_loader.load_expert(expert))
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # Jamba専用の分岐をなくし、一貫したtemperatureを設定
        output: Any = llm.create_chat_completion(
            messages=messages,
            max_tokens=4096,
            temperature=0.2, # 安定した応答のため低めに設定
            stop=["<|im_end|>", "</s>", "<|endoftext|>"]
        )
        
        if (
            "choices" in output and 
            isinstance(output["choices"], list) and 
            output["choices"] and
            "message" in output["choices"][0] and
            isinstance(output["choices"][0]["message"], dict) and
            "content" in output["choices"][0]["message"] and
            isinstance(output["choices"][0]["message"]["content"], str)
        ):
            return output["choices"][0]["message"]["content"].strip()
        
        print(f"⚠️ 警告: エキスパート '{expert.name}' から予期せぬ形式の応答がありました。 Response: {output}")
        return ""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️