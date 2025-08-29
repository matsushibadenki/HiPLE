# ./agents/wikipedia_agent.py
# このコードは、Wikipediaでの検索と結果の要約を担当します。ユーザーの質問から最適な検索キーワードを抽出する機能を追加し、検索精度を向上させました。

from typing import List
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel
from services.wikipedia_service import WikipediaService
from services.model_loader import ModelLoaderService
from llama_cpp.llama_types import ChatCompletionRequestMessage

class WikipediaAgent(BaseAgent):
    """
    Wikipediaを検索し、結果をLLMで要約・整形して返すエージェント。
    """
    def __init__(self, model_loader: ModelLoaderService):
        super().__init__(model_loader)
        self.wikipedia_service = WikipediaService(lang="ja")

    def execute(self, query: str, all_experts: List[ExpertModel]) -> str:
        """
        指定されたクエリでWikipediaを検索し、結果を要約・整形して返す。
        """
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # LLMを使って、検索に最適なキーワードを抽出する
        summarizer_expert = self._find_expert("HRM", all_experts)
        search_term = self._extract_search_term(query, summarizer_expert)
        print(f"🔍 抽出された検索キーワード: '{search_term}'")

        print(f"📖 Wikipediaで '{search_term}' を検索しています...")
        search_results = self.wikipedia_service.search(search_term)
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        if not search_results:
            return f"'{query}' に関するWikipedia記事は見つかりませんでした。"

        first_title = search_results[0]
        print(f"📄 最も関連性の高い記事 '{first_title}' の要約を取得します。")
        raw_summary = self.wikipedia_service.get_summary(first_title, sentences=15)

        if not raw_summary:
            return f"記事 '{first_title}' の要約を取得できませんでした。"

        # 取得した要約を、論理的整理が得意なHRMに渡して整形させる
        print(f"✍️ 取得した情報をHRMで整形・要約します...")
        
        system_prompt = "あなたは、与えられたWikipediaの記事の抜粋を分析し、最も重要なポイントを抽出して、人間にとって非常に分かりやすい形式に再構成する優秀な編集者です。"
        user_prompt = f"""以下のテキストを読み、重要なポイントを抽出し、箇条書きなどを用いて簡潔で明瞭なサマリーを作成してください。数式や不要な記号は取り除き、平易な言葉で説明してください。

# 元のテキスト
---
{raw_summary}
---

# あなたのタスク
上記のテキストの核心を捉えた、分かりやすいサマリーを生成してください。
"""
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        formatted_summary = self._query_llm(summarizer_expert, messages)
        
        return f"Wikipediaの記事「{first_title}」の要約:\n\n{formatted_summary}"

    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    def _extract_search_term(self, query: str, expert: ExpertModel) -> str:
        """
        ユーザーの質問文から、Wikipedia検索に最適な名詞句や専門用語を抽出する。
        """
        system_prompt = "ユーザーの質問文から、百科事典（Wikipedia）で検索するのに最も適した、中心的で具体的なキーワード（名詞句や専門用語）を一つだけ抽出してください。回答は、抽出したキーワードのみを含めてください。余計な説明や挨拶は一切不要です。"
        user_prompt = f"以下の文章から検索キーワードを抽出してください:\n\n「{query}」"
        
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # LLMを呼び出してキーワードを抽出
        extracted_term = self._query_llm(expert, messages)
        
        # 不要な引用符や装飾を削除
        return extracted_term.strip().replace('"', '').replace("'", "")
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        """特定のエキスパートを見つける。"""
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")