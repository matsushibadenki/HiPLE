# path: ./agents/base_agent.py
# title: Base Agent with Self-Evaluation Capability (Corrected)
# description: 全てのエージェントの基盤。LLMからの応答と自己評価（自信度・理由）をJSON形式で受け取る。

from abc import ABC, abstractmethod
import json
import re
from typing import List, Any, Optional, cast, Dict
from llama_cpp import Llama
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from services.model_loader import ModelLoaderService

class BaseAgent(ABC):
    """
    すべてのエージェントの基本となる抽象基底クラス。
    自己評価機能を組み込んでいる。
    """
    def __init__(self, model_loader: ModelLoaderService):
        self.model_loader = model_loader

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """エージェントの主処理を実行するメソッド"""
        pass

    def _add_self_evaluation_prompt(self, system_prompt: str) -> str:
        """システムプロンプトに自己評価を促す指示を追加する"""
        evaluation_prompt = """
# 自己評価
あなたの応答が完了したら、必ず以下のJSON形式で自己評価を追加してください。

```json
{
  "response": "（ここにあなたの主たる応答を記述）",
  "self_evaluation": {
    "confidence": "（あなたの応答に対する自信度を0.0から1.0の数値で評価）",
    "reasoning": "（その自信度に至った理由や、応答の限界、注意点を簡潔に説明）"
  }
}
```
"""
        return system_prompt + "\n" + evaluation_prompt

    def _query_llm(self, expert: ExpertModel, messages: List[ChatCompletionRequestMessage]) -> Dict[str, Any]:
        """LLMに問い合わせを実行し、応答と自己評価をパースして返す"""
        llm = cast(Llama, self.model_loader.load_expert(expert))
        
        if messages and messages[0]["role"] == "system":
            original_prompt = cast(str, messages[0]["content"])
            if "content" in messages[0] and isinstance(messages[0]["content"], str):
                 messages[0]["content"] = self._add_self_evaluation_prompt(messages[0]["content"])


        output: Any = llm.create_chat_completion(
            messages=messages,
            max_tokens=4096,
            temperature=0.2,
            stop=["<|im_end|>", "</s>", "<|endoftext|>"]
        )
        
        raw_response = ""
        if (
            "choices" in output and isinstance(output["choices"], list) and output["choices"] and
            "message" in output["choices"][0] and isinstance(output["choices"][0]["message"], dict) and
            "content" in output["choices"][0]["message"] and isinstance(output["choices"][0]["message"]["content"], str)
        ):
            raw_response = output["choices"][0]["message"]["content"].strip()
        
        if not raw_response:
            return {"response": "", "self_evaluation": {"confidence": 0.0, "reasoning": "No response from LLM."}}

        try:
            json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_response, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                start_index = raw_response.find('{')
                end_index = raw_response.rfind('}')
                if start_index != -1 and end_index != -1:
                    json_str = raw_response[start_index:end_index + 1]
                else:
                    return {"response": raw_response, "self_evaluation": {"confidence": 0.5, "reasoning": "Could not parse JSON structure."}}

            data = json.loads(json_str)
            
            response = data.get("response", raw_response)
            evaluation = data.get("self_evaluation", {"confidence": 0.5, "reasoning": "Evaluation data missing."})

            if not isinstance(evaluation.get("confidence"), (int, float)):
                evaluation["confidence"] = 0.5

            return {"response": response, "self_evaluation": evaluation}

        except (json.JSONDecodeError, KeyError):
            return {"response": raw_response, "self_evaluation": {"confidence": 0.5, "reasoning": "Failed to parse self-evaluation JSON."}}
