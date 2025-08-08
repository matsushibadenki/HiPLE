# path: ./agents/tool_router_agent.py
# title: Tool Router Agent
# description: ユーザーの要求を分析し、最適なツール（Web検索、Wikipedia検索、ツール不要）を選択するエージェント。

from typing import List
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class ToolRouterAgent(BaseAgent):
    """
    ユーザーの要求を分析し、適切なツールを選択するインテリジェントなルーター。
    """
    def execute(self, prompt: str, experts: List[ExpertModel]) -> str:
        """
        プロンプトを分析し、'wikipedia', 'web_search', 'no_tool', 'complex_task' のいずれかを返す。
        """
        router_expert = self._find_expert("HRM", experts)

        system_prompt = """あなたはユーザーの要求を分析し、その要求を達成するために最も適したツールを判断する、優秀なディスパッチャーです。
以下の選択肢の中から、最も適切だと思われるものを一つだけ選んで、そのキーワード（例: 'wikipedia'）のみを答えてください。

# 選択肢
- `wikipedia`: 特定の人物、場所、出来事、専門用語など、百科事典的な知識が求められている場合。（例：「徳川家康について教えて」「量子コンピュータとは何ですか？」）
- `web_search`: 最新のニュース、トレンド、特定の製品のレビュー、株価など、リアルタイム性や網羅性が重要な情報が求められている場合。（例：「今日の東京の天気は？」「最新のAIニュースを調べて」）
- `complex_task`: コードの生成、画像の作成、複数ステップにわたる複雑な指示、創造的な文章の執筆など、単一の検索では完結しないタスクの場合。（例：「PythonでWebサーバーを実装して」「悲しい物語を書いて」）
- `no_tool`: 上記のいずれにも当てはまらない、一般的な挨拶や単純な対話の場合。（例：「こんにちは」「ありがとう」）

ユーザーの要求を慎重に読み、上記の4つのキーワードの中から最もふさわしいものを一つだけ選んでください。余計な説明は一切不要です。
"""

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        response = self._query_llm(router_expert, messages).lower().strip()

        # 応答からキーワードを抽出
        if "wikipedia" in response:
            return "wikipedia"
        if "web_search" in response:
            return "web_search"
        if "complex_task" in response:
            return "complex_task"
        
        return "no_tool"

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")