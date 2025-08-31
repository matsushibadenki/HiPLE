# path: ./agents/wikipedia_agent.py
# title: Wikipedia Agent (Improved Keyword Extraction)
# description: Extracts Japanese keywords with high precision to improve search accuracy.

from typing import List, Dict, Any, Optional
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
        summarizer_expert = self._find_expert("HRM", all_experts)
        if not summarizer_expert:
             return "エラー: Wikipedia検索に必要なHRMエキスパートが見つかりません。"

        search_term_data = self._extract_search_term(query, summarizer_expert)
        search_term = search_term_data.get("response", query) # 抽出失敗時は元のクエリを使用
        
        print(f"🔍 抽出された検索キーワード: '{search_term}'")

        print(f"📖 Wikipediaで '{search_term}' を検索しています...")
        search_results = self.wikipedia_service.search(search_term)

        if not search_results:
            return f"「{query}」に関するWikipedia記事は見つかりませんでした。"

        first_title = search_results[0]
        print(f"📄 最も関連性の高い記事「{first_title}」の要約を取得します。")
        raw_summary = self.wikipedia_service.get_summary(first_title, sentences=15)

        if not raw_summary:
            return f"記事「{first_title}」の要約を取得できませんでした。"

        print(f"✍️ 取得した情報をHRMで整形・要約します...")
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        system_prompt = "あなたは、与えられたWikipediaの記事の抜粋を分析し、ユーザーの元の質問に対して、ステップバイステップで分かりやすく具体的な手順を説明する優秀な解説者です。"
        user_prompt = f"""以下のテキストは、Wikipediaの記事「{first_title}」からの抜粋です。
この情報を基に、ユーザーからの最初の質問に直接回答する形で、簡潔で明瞭なサマリーを作成してください。

# ユーザーの最初の質問
「{query}」

# 記事の抜粋
---
{raw_summary}
---

# あなたのタスク
上記の抜粋から、ユーザーの質問に答えるために必要な情報だけを抽出し、**具体的な材料と作り方の手順がわかるように**、箇条書きなどを用いて分かりやすい最終的な回答を生成してください。
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        formatted_summary_data = self._query_llm(summarizer_expert, messages)
        formatted_summary = formatted_summary_data.get("response", "要約の生成に失敗しました。")
        
        return f"Wikipediaの記事「{first_title}」を基にした回答:\n\n{formatted_summary}"

    def _extract_search_term(self, query: str, expert: ExpertModel) -> Dict[str, Any]:
        """
        ユーザーの質問文から、日本語Wikipediaの検索に最適な日本語のキーワードを抽出する。
        """
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        system_prompt = """あなたは、ユーザーの質問の核心を理解し、日本語の百科事典（Wikipedia）で調べるのに最も適した、具体的で短い「日本語の検索キーワード」を抽出する専門家です。
例えば、「アイスの作り方」という質問であれば、「アイスクリーム 製造」や「氷菓」のような、製造方法や分類に関するキーワードが適切です。
回答は、抽出したキーワード本体のみを含むようにしてください。余計な説明や挨拶、JSONの定型文は一切不要です。
"""
        user_prompt = f"以下の質問文から、日本語のWikipediaで検索するための最も的確なキーワードを一つだけ抽出してください:\n\n「{query}」"
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        response_data = self._query_llm(expert, messages)
        
        # LLMが自己評価のJSON構造を返してしまった場合でも、キーワード本体を抽出する
        response_text = response_data.get("response", "")
        if isinstance(response_text, dict):
            response_text = response_text.get("keyword", "") or str(response_text)

        # 不要な引用符や装飾を削除
        cleaned_term = response_text.strip().replace('"', '').replace("'", "").replace("`", "")
        response_data["response"] = cleaned_term
        return response_data

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> Optional[ExpertModel]:
        """特定のエキスパートを見つける。"""
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        return None