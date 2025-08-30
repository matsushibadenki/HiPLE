# path: ./orchestrator/router.py
# title: Simple Router with Emergent Task Recognition
# description: A simple, keyword-based router that now recognizes requests for brainstorming.

from typing import Dict, Any, List

class SimpleRouter:
    """
    キーワードとヒューリスティクスに基づいてユーザーの要求をルーティングする、
    LLMに依存しないシンプルなルーター。
    """
    def __init__(self):
        self.greetings: Dict[str, str] = {
            "こんにちは": "こんにちは！何かお役に立てることはありますか？",
            "おはよう": "おはようございます！良い一日を。",
            "こんばんは": "こんばんは。いかがお過ごですか？",
            "ありがとう": "どういたしまして！"
        }
        
        self.tool_keywords: Dict[str, List[str]] = {
            "emergent_task": ["ブレインストーミング", "ブレストして", "新しいアイデア", "革新的な", "創造的な解決策", "発想して"],
            "wikipedia": ["教えて", "とは", "誰", "何", "どこ", "原理", "メカニズム", "歴史", "について"],
            "complex_task": ["作成して", "実装して", "分析して", "書いて", "作って", "計画して", "要約して", "翻訳して", "比較して"]
        }

    def route(self, prompt: str) -> Dict[str, Any]:
        """
        プロンプトを分析し、タスクの種類とクエリを決定する。
        """
        normalized_prompt = prompt.strip().lower()

        # 1. 挨拶のチェック
        for greeting, response in self.greetings.items():
            if greeting in normalized_prompt:
                return {"type": "greeting", "response": response}

        # 2. ツールキーワードのチェック (創発タスクを先に評価)
        for tool, keywords in self.tool_keywords.items():
            for keyword in keywords:
                if keyword in normalized_prompt:
                    if tool == "wikipedia":
                        return {"type": "wikipedia", "query": prompt}
                    elif tool == "emergent_task":
                        return {"type": "emergent_task", "query": prompt}
                    
                    query = prompt.replace(keyword, "").strip()
                    return {"type": tool, "query": query if query else prompt}

        # 3. 上記に当てはまらない場合は、複雑なタスクとして計画立案に回す
        return {"type": "complex_task", "query": prompt}
