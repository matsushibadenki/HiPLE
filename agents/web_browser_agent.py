# path: ./agents/web_browser_agent.py
# title: Web Browser Agent (Synchronous)
# description: WebBrowserServiceを使い、レンダリングされたWebページを調査・分析するエージェント。

from typing import List
from bs4 import BeautifulSoup, NavigableString
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel
from llama_cpp.llama_types import ChatCompletionRequestMessage
import re

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
        for tag in soup(['script', 'style', 'nav', 'footer', 'aside', 'header', 'link', 'meta']):
            tag.decompose()
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # クエリに関連するキーワードでテキストを絞り込む
        keywords = re.split(r'\s+', query) + ["材料", "作り方", "レシピ", "手順"]
        
        relevant_text = ""
        for element in soup.find_all(string=True):
            if isinstance(element, NavigableString):
                parent = element.parent
                # 親要素が存在し、表示されている要素のみを対象とする
                if parent and parent.name not in ['script', 'style', 'head', 'title']:
                    text_line = element.strip()
                    if any(keyword in text_line for keyword in keywords):
                        # 関連キーワードが含まれる行の周辺テキストを取得
                        context_lines = []
                        # 前後の兄弟要素からテキストを取得して文脈を追加
                        for sibling in element.find_previous_siblings(limit=2):
                            context_lines.insert(0, sibling.get_text(separator=' ', strip=True))
                        context_lines.append(text_line)
                        for sibling in element.find_next_siblings(limit=2):
                            context_lines.append(sibling.get_text(separator=' ', strip=True))
                        
                        relevant_text += " ".join(context_lines) + "\n"
        
        if not relevant_text:
            body_text = soup.get_text(separator='\n', strip=True)
            if not body_text:
                return "エラー: ページからテキストコンテンツを抽出できませんでした。"
            relevant_text = body_text
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        # コンテキストウィンドウを考慮してテキストを切り詰める
        max_length = 8000
        truncated_text = relevant_text[:max_length]

        # 要約には論理的推論が得意なHRMを指名
        summarizer_expert = self._find_expert("HRM", all_experts)
        
        return self._summarize_with_llm(summarizer_expert, truncated_text, query)

    def _summarize_with_llm(self, expert: ExpertModel, text: str, query: str) -> str:
        """LLMを使ってテキストを要約する。"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        system_prompt = "あなたは、与えられたWebページのテキストコンテンツを分析し、ユーザーの質問に的確に答える優秀なアナリストです。テキストの中から関連する情報のみを抽出し、具体的なレシピや手順がわかるように要約してください。"
        user_prompt = f"""以下のWebページの内容を読み、質問に答えてください。

# 質問
{query}

# Webページの内容 (関連部分抜粋)
---
{text}
---

質問に対する回答を、**材料と作り方の手順が明確にわかるように箇条書きで**生成してください。
もし情報が不足していて回答できない場合は、「ウェブページから具体的な作り方を見つけることができませんでした。」と正直に回答してください。
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        response_data = self._query_llm(expert, messages)
        return response_data.get("response", "要約の生成に失敗しました。")
    
    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        """特定のエキスパートを見つける。"""
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")