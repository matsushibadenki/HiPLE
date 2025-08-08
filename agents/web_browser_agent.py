# path: ./agents/web_browser_agent.py
# title: Web Browser Agent
# description: WebBrowserServiceを使い、レンダリングされたWebページを調査・分析するエージェント。

from typing import List, Dict, Any
from bs4 import BeautifulSoup
from llama_cpp.llama_types import ChatCompletionRequestMessage
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel
from services.web_browser_service import WebBrowserService
from services.model_loader import ModelLoaderService


class WebBrowserAgent(BaseAgent):
    """
    Webページを調査し、その内容を分析・要約するエージェント。
    """
    def __init__(self, model_loader: ModelLoaderService):
        super().__init__(model_loader)
        self.browser_service = WebBrowserService()

    async def execute(self, url: str, query: str, all_experts: List[ExpertModel]) -> str:
        """
        指定されたURLを調査し、クエリに基づいて内容を要約する。
        """
        try:
            await self.browser_service.launch_browser()
            html_content = await self.browser_service.get_page_content(url)
            
            if html_content.startswith("エラー:"):
                return html_content

            # BeautifulSoupでHTMLから主要なテキストを抽出
            soup = BeautifulSoup(html_content, 'html.parser')
            for script in soup(["script", "style"]):
                script.decompose()
            body_text = soup.get_text(separator='\n', strip=True)
            
            if not body_text:
                return "エラー: ページからテキストコンテンツを抽出できませんでした。"

            # テキストが長すぎる場合、主要部分を切り出す（ここでは単純に文字数で制限）
            max_length = 8000 # LLMのコンテキスト長を考慮
            truncated_text = body_text[:max_length]

            # HRMエキスパートに要約を依頼
            summarizer_expert = self._find_expert("HRM", all_experts)
            if not summarizer_expert:
                return "エラー: 要約担当のエキスパート'HRM'が見つかりません。"
            
            summary = self._summarize_with_llm(summarizer_expert, truncated_text, query)
            return summary

        except Exception as e:
            return f"WebBrowserAgentの実行中にエラーが発生しました: {e}"
        finally:
            await self.browser_service.close_browser()

    def _summarize_with_llm(self, expert: ExpertModel, text: str, query: str) -> str:
        """LLMを使ってテキストを要約する。"""
        system_prompt = "あなたは、与えられたWebページのテキストコンテンツを分析し、ユーザーの質問に的確に答える優秀なアナリストです。テキストの中から関連する情報のみを抽出し、簡潔にまとめてください。"
        user_prompt = f"""以下のWebページの内容を読み、質問に答えてください。

# 質問
{query}

# Webページの内容
---
{text}
---

質問に対する回答を生成してください。
"""
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        return self._query_llm(expert, messages)
    
    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        """特定のエキスパートを見つける。"""
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")