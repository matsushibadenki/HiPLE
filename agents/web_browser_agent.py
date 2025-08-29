# path: ./agents/web_browser_agent.py
# title: Web Browser Agent (Synchronous)
# description: WebBrowserServiceを使い、レンダリングされたWebページを調査・分析するエージェント。

from typing import List
from bs4 import BeautifulSoup
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel
from llama_cpp.llama_types import ChatCompletionRequestMessage

class WebBrowserAgent(BaseAgent):
    """
    Webページを調査し、その内容を分析・要約するエージェント。
    """
    def execute(self, content: str, query: str, all_experts: List[ExpertModel]) -> str:
        """
        指定されたHTMLコンテンツを分析し、クエリに基づいて内容を要約する。
        """
        if "エラー:" in content:
            return content

        soup = BeautifulSoup(content, 'html.parser')
        for tag in soup(['script', 'style', 'nav', 'footer', 'aside', 'header']):
            tag.decompose()
        
        body_text = soup.get_text(separator='\n', strip=True)
        if not body_text:
            return "エラー: ページからテキストコンテンツを抽出できませんでした。"

        # コンテキストウィンドウを考慮してテキストを切り詰める
        max_length = 8000
        truncated_text = body_text[:max_length]

        # 要約には論理的推論が得意なHRMを指名
        summarizer_expert = self._find_expert("HRM", all_experts)
        
        return self._summarize_with_llm(summarizer_expert, truncated_text, query)

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
