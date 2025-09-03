# path: ./agents/web_browser_agent.py
# title: Web Browser Agent (LLM-Powered Recipe Extractor)
# description: Uses a dedicated LLM call to intelligently extract only recipe information from raw HTML, providing clean data to subsequent agents.

from bs4 import BeautifulSoup
from typing import List
from llama_cpp.llama_types import ChatCompletionRequestMessage
from services.model_loader import ModelLoaderService
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class WebBrowserAgent(BaseAgent):
    """
    Webページを解析し、LLMを使ってレシピ情報（材料と手順）を抽出するエージェント。
    BaseAgentを継承し、標準的な方法でLLMを呼び出す。
    """
    def __init__(self, model_loader: ModelLoaderService):
        """
        Args:
            model_loader (ModelLoaderService): LLMモデルをロードするためのサービス。
        """
        super().__init__(model_loader)

    def execute(self, content: str, query: str, experts: List[ExpertModel]) -> str:
        """
        指定されたHTMLコンテンツからLLMを使ってレシピ情報を抽出する。

        Args:
            content (str): 解析対象のHTMLコンテンツ。
            query (str): 元の検索クエリ。
            experts (List[ExpertModel]): 利用可能なエキスパートのリスト。

        Returns:
            str: 抽出されたレシピ情報、またはエラーメッセージ。
        """
        if "エラー:" in content:
            return content

        soup = BeautifulSoup(content, 'html.parser')
        for tag in soup(['script', 'style', 'nav', 'footer', 'aside', 'header', 'link', 'meta', 'form', 'button', 'input']):
            tag.decompose()
        
        body_text = soup.get_text(separator='\n', strip=True)
        if not body_text:
            return "エラー: ページからテキストコンテンツを抽出できませんでした。"

        # コンテキスト量を考慮してテキストを切り詰める
        max_length = 12000
        truncated_text = body_text[:max_length]

        summarizer_expert = self._find_summarizer_expert(experts)
        
        system_prompt = "あなたは、与えられたテキストから最も重要な情報だけを抽出する専門家です。"
        user_prompt = f"""以下のWebページテキストから、料理の「材料」と「作り方（手順）」に関する記述のみを抽出し、箇条書きで分かりやすくまとめてください。
ウェブサイトのナビゲーション、広告、関連リンク、コメントなど、レシピ以外の余分な情報はすべて完全に無視・削除してください。

--- Webページテキスト ---
{truncated_text}
---
"""
        
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        try:
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            # 標準的な_query_llmメソッドを使用するように修正
            response_data = self._query_llm(summarizer_expert, messages)
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️
            clean_recipe = response_data.get("response", "レシピの抽出に失敗しました。")
            return clean_recipe if clean_recipe else "レシピ情報が見つかりませんでした。"
        except Exception as e:
            print(f"WebBrowserAgent内でLLM呼び出しエラー: {e}")
            return f"エラー: レシピ情報の抽出中に問題が発生しました - {e}"

    def _find_summarizer_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        """要約に適したエキスパートを見つける（Jambaを優先）"""
        for expert in experts:
            if expert.name.lower() == "jamba":
                return expert
        # フォールバックとしてHRMを探す
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        # それでも見つからない場合は最初のエキスパートを利用
        if experts:
            return experts[0]
        raise ValueError("利用可能なエキスパートが見つかりません。")

