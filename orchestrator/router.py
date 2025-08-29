# /matsushibadenki/hiple/HiPLE-6a124133fd7537b5a7a4c8834c276a4900c47121/orchestrator/router.py
# このコードは、ユーザーの要求を分析し、適切な機能へ振り分ける役割を担います。Wikipedia検索の精度を向上させるため、検索クエリの生成ロジックを修正しました。

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
        
        # 各ツールに関連付けられたキーワード
        self.tool_keywords: Dict[str, List[str]] = {
            "wikipedia": ["教えて", "とは", "誰", "何", "どこ", "原理", "メカニズム", "歴史", "について"],
            "complex_task": ["作成して", "実装して", "分析して", "書いて", "作って", "計画して", "要約して", "翻訳して", "比較して"]
        }

    def route(self, prompt: str) -> Dict[str, Any]:
        """
        プロンプトを分析し、タスクの種類とクエリを決定する。

        Returns:
            Dict[str, Any]: e.g., {"type": "greeting", "response": "こんにちは！"}
                            or {"type": "wikipedia", "query": "量子もつれ"}
                            or {"type": "complex_task", "query": prompt}
                            or {"type": "simple_chat", "query": prompt}
        """
        normalized_prompt = prompt.strip().lower()

        # 1. 挨拶のチェック
        for greeting, response in self.greetings.items():
            if greeting in normalized_prompt:
                return {"type": "greeting", "response": response}

        # 2. ツールキーワードのチェック
        for tool, keywords in self.tool_keywords.items():
            for keyword in keywords:
                if keyword in normalized_prompt:
                    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
                    # Wikipediaの場合は、検索精度向上のため元のプロンプト全体をクエリとして渡す
                    if tool == "wikipedia":
                        return {"type": "wikipedia", "query": prompt}
                    
                    # それ以外のツールはキーワードを除いた部分をクエリとして抽出することを試みる
                    query = prompt.replace(keyword, "").strip()
                    return {"type": tool, "query": query if query else prompt}
                    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        # 3. 上記に当てはまらない場合は、複雑なタスクとして計画立案に回す
        return {"type": "complex_task", "query": prompt}
