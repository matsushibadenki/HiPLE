# path: ./agents/tool_router_agent.py
# title: Tool Router Agent
# description: ユーザーの要求を分析し、最適なツール（Web検索、Wikipedia検索、ツール不要）と検索キーワードをJSON形式で特定するエージェント。

import json
import re
from typing import List, Dict, Any
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class ToolRouterAgent(BaseAgent):
    """
    ユーザーの要求を分析し、適切なツールと検索クエリを特定するインテリジェントなルーター。
    """
    def execute(self, prompt: str, experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        プロンプトを分析し、ツールと検索クエリを含む辞書を返す。
        例: {"tool": "wikipedia", "query": "猫"}
        """
        router_expert = self._find_expert("HRM", experts)

        system_prompt = """あなたはユーザーの要求を分析し、その要求を達成するために最も適したツールと、そのツールで検索すべきキーワードを判断する、優秀なディスパッチャーです。
以下のJSONフォーマットで、判断結果のみを答えてください。余計な説明は一切不要です。

# 出力フォーマット
```json
{
  "tool": "（'wikipedia', 'web_search', 'complex_task', 'no_tool' のいずれか）",
  "query": "（ツールを使用する場合に検索すべきキーワード。ツール不要の場合はnull）"
}
```

# 判断基準
- `wikipedia`: 特定の人物、場所、出来事、専門用語など、百科事典的な知識が求められている場合。`query`にはその固有名詞を指定します。（例：ユーザー要求「徳川家康について教えて」 -> query: "徳川家康"）
- `web_search`: 最新のニュース、トレンド、製品レビューなど、リアルタイム性や網羅性が重要な情報が求められている場合。`query`には検索フレーズを指定します。（例：ユーザー要求「今日の東京の天気は？」 -> query: "東京 天気"）
- `complex_task`: コード生成、画像作成、複数ステップの指示、創造的な文章執筆など、単一の検索では完結しないタスクの場合。`query`はnullにします。
- `no_tool`: 一般的な挨拶や単純な対話の場合。`query`はnullにします。

ユーザーの要求を慎重に読み、上記のJSON形式で応答してください。
"""

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        raw_response = self._query_llm(router_expert, messages)
        
        try:
            # 応答からJSONを抽出
            json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_response, re.DOTALL)
            if json_match:
                response_json_str = json_match.group(1)
            else:
                # 生のJSONオブジェクトのフォールバック
                response_json_str = raw_response[raw_response.find('{'):raw_response.rfind('}')+1]

            data = json.loads(response_json_str)
            tool = data.get("tool", "no_tool")
            query = data.get("query")

            # 基本的な検証
            if tool not in ["wikipedia", "web_search", "complex_task", "no_tool"]:
                tool = "no_tool"

            return {"tool": tool, "query": query if query else prompt}

        except (json.JSONDecodeError, AttributeError):
            # パースに失敗した場合、後方互換性のために単純なキーワードマッチングにフォールバック
            response_lower = raw_response.lower()
            if "wikipedia" in response_lower:
                return {"tool": "wikipedia", "query": prompt} # Fallback
            if "web_search" in response_lower:
                return {"tool": "web_search", "query": prompt} # Fallback
            if "complex_task" in response_lower:
                return {"tool": "complex_task", "query": prompt}
            return {"tool": "no_tool", "query": prompt}

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")
