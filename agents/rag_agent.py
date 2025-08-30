# path: ./agents/rag_agent.py
# title: RAG Agent (Self-Evaluation Aware)
# description: Determines if retrieval is necessary and provides self-evaluated decision.

import json
import re
from typing import List, Dict, Any
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class RAGAgent(BaseAgent):
    """
    与えられたプロンプトに対して、内部知識ベースの検索(RAG)が必要かどうか、
    また検索する場合の最適なクエリは何かを判断するエージェント。
    """
    def execute(self, prompt: str, experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        プロンプトを分析し、検索の要否と検索クエリを含む辞書を返す。
        """
        router_expert = self._find_expert("HRM", experts)

        system_prompt = """あなたはユーザーのタスク記述を分析し、そのタスクを達成するために内部知識ベース（過去の計画やタスクの文脈）の検索が必要かどうかを判断する、優秀なアシスタントです。
以下のJSONフォーマットで、判断結果のみを答えてください。余計な説明は一切不要です。

# 出力フォーマット
```json
{
  "needs_retrieval": "（trueまたはfalse）",
  "query": "（検索が必要な場合に、内部知識ベースを検索するための最も的確なキーワードや質問文。検索不要の場合はnull）"
}
```

# 判断基準
- `needs_retrieval: true`: タスクが先行するタスクの結果や、計画全体の目標、他のマイルストーンなど、過去の文脈情報を明確に必要としている場合。`query`には、その文脈を最もよく表すキーワードを指定します。（例：タスク「上記の結果を要約する」 -> query: "先行タスクの結果"）
- `needs_retrieval: false`: タスクが自己完結しており、外部の文脈情報なしに実行可能な場合。（例：タスク「Pythonで'Hello World'を出力するコードを書く」）

ユーザーのタスク記述を慎重に読み、上記のJSON形式を、自己評価JSONの`response`キーに含めて応答してください。
"""

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        response_data = self._query_llm(router_expert, messages)
        
        # 応答がJSON文字列で返ってくる場合があるため、パースを試みる
        raw_response_content = response_data.get("response", "{}")
        try:
            if isinstance(raw_response_content, str):
                 # LLMがresponseキーの中にさらにJSON文字列を生成する場合がある
                json_match = re.search(r'\{[\s\S]*\}', raw_response_content)
                if json_match:
                    decision_json = json.loads(json_match.group(0))
                else:
                    decision_json = {}
            else:
                decision_json = raw_response_content

            needs_retrieval = decision_json.get("needs_retrieval", False)
            if not isinstance(needs_retrieval, bool):
                needs_retrieval = str(needs_retrieval).lower() == 'true'
            
            query = decision_json.get("query") if needs_retrieval else None
            
            response_data["response"] = {"needs_retrieval": needs_retrieval, "query": query}
        
        except (json.JSONDecodeError, AttributeError):
             response_data["response"] = {"needs_retrieval": False, "query": None}
        
        return response_data


    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")
