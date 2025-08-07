# path: ./agents/router_agent.py
# title: Router Agent
# description: ユーザーの要求が単純か複雑かを判断するエージェント

from typing import List
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class RouterAgent(BaseAgent):
    """
    ユーザーの要求を分析し、単純な応答で十分か、
    複雑な計画が必要かを判断するエージェント。
    """
    def execute(self, prompt: str, experts: List[ExpertModel]) -> str:
        """
        プロンプトを分析し、'simple' または 'complex' を返す。
        """
        # ルーティングには論理的判断が得意なHRMモデルを利用
        router_expert = self._find_expert("HRM", experts)
        
        expert_descriptions = "\n".join([f"- {e.name}: {e.description}" for e in experts])

        system_prompt = f"""あなたはユーザーの要求を分析し、その要求が「単純な質問」か「複雑なタスク」かを判断するルーターです。
- 「単純な質問」とは、単一のエキスパートが一度の応答で完結できる質問です。（例：「〜とは何ですか？」「〜を教えて」）
- 「複雑なタスク」とは、複数のステップや、異なるエキスパートの連携、ファイルの生成が必要な要求です。（例：「〜を分析してレポートを作成し、画像を生成してください」）

利用可能なエキスパート:
{expert_descriptions}

ユーザーの要求を読み、"simple" または "complex" のいずれか一言だけで応答してください。
"""

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        
        response = self._query_llm(router_expert, messages).lower()
        
        if "complex" in response:
            return "complex"
        return "simple"

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")