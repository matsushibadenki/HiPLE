# path: ./agents/wikipedia_agent.py
# title: Wikipedia Agent (mypy compatible)
# description: WikipediaServiceを利用して、特定のトピックに関する情報を検索・要約するエージェント。mypyエラーを修正。

from typing import List, Dict, Any
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel
from services.wikipedia_service import WikipediaService
from services.model_loader import ModelLoaderService
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from llama_cpp.llama_types import ChatCompletionRequestMessage
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

class WikipediaAgent(BaseAgent):
    """
    Wikipediaを検索し、結果を要約して返すエージェント。
    """
    def __init__(self, model_loader: ModelLoaderService):
        super().__init__(model_loader)
        self.wikipedia_service = WikipediaService(lang="ja")

    def execute(self, query: str) -> str:
        """
        指定されたクエリでWikipediaを検索し、見つかった最初の記事の要約を返す。
        """
        print(f"📖 Wikipediaで '{query}' を検索しています...")
        search_results = self.wikipedia_service.search(query)

        if not search_results:
            return f"'{query}' に関するWikipedia記事は見つかりませんでした。"

        first_title = search_results[0]
        print(f"📄 最も関連性の高い記事 '{first_title}' の要約を取得します。")
        summary = self.wikipedia_service.get_summary(first_title, sentences=10)

        if not summary:
            return f"記事 '{first_title}' の要約を取得できませんでした。"

        return f"Wikipediaから得られた '{first_title}' の要約:\n\n{summary}"

    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    # 親クラスとシグネチャを合わせる
    def _query_llm(self, expert: ExpertModel, messages: List[ChatCompletionRequestMessage]) -> str:
        # このエージェントはLLMを直接使用しないため、実装は不要
        raise NotImplementedError("WikipediaAgent does not use LLM directly.")
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
