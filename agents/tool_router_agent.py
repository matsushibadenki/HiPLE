# path: ./agents/tool_router_agent.py
# title: Tool Router Agent with Chain-of-Thought Prompting
# description: ユーザーの要求を分析し、最適なツールを特定するエージェント。思考プロセスを導入したプロンプトで判断精度を最大化する。

import json
import re
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class ToolRouterAgent(BaseAgent):
    """
    ユーザーの要求を分析し、適切なツールと検索クエリを特定するインテリジェントなルーター。
    """
    def execute(self, prompt: str, experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        プロンプトを分析し、ツール、検索クエリ、URLを含む辞書を返す。
        """
        router_expert = self._find_router_expert(experts)
        print(f"🧠 Router expert selected: {router_expert.name}")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        system_prompt = """あなたはユーザーの要求を分析し、その要求を達成するために最も適したツールを判断する、超優秀なディスパッチャーです。
以下の思考プロセスに従い、最終的な判断をJSONフォーマットで出力してください。

# 思考プロセス (Step-by-Step)
1.  **要求の核心を分析**: ユーザーは何を求めているか？ (例: 「定義を知りたい」「最新情報が欲しい」「何かを作ってほしい」)
2.  **時間の重要性を評価**: その情報は時間と共に変化するか？ (例: 「天気」は変化する、「徳川家康」は変化しない)
3.  **ツールの選択**: 上記の分析に基づき、以下の基準で最適なツールを一つだけ選択する。
4.  **JSON生成**: 最終的な判断をJSON形式で出力する。思考プロセスは出力に含めないこと。

# 判断基準
- `wikipedia`: **「普遍的で確立された知識」**が求められている場合。特定の固有名詞、専門用語、歴史上の出来事など、**時間が経っても内容が変わらない**情報。
    - 例: 「徳川家康」「量子もつれ」「エッフェル塔」
- `web_search`: **「リアルタイム性・網羅性」**が重要な情報が求められている場合。最新のニュース、トレンド、製品レビュー、特定のURLの要約など、**時間と共に変化する**情報。
    - 例: 「今日の天気」「最新のAIニュース」「この記事(URL)の要約」
- `complex_task`: **「生成・実行」**が求められている場合。コード生成、画像作成、複数ステップの指示、創造的な文章執筆など、単一の検索では完結しないタスク。
    - 例: 「PythonでWebサーバーを実装」「猫の画像を作成」
- `no_tool`: **「単純な対話」**の場合。一般的な挨拶や短い会話。
    - 例: 「こんにちは」「ありがとう」

# 出力フォーマット (厳守)
```json
{
  "tool": "（'wikipedia', 'web_search', 'complex_task', 'no_tool' のいずれか）",
  "query": "（ツールを使用する場合に検索すべきキーワード。ツール不要の場合はnull）",
  "url": "（web_searchの場合にアクセスすべきURL。それ以外はnull）"
}
```

ユーザーの要求を上記の思考プロセスに従って慎重に分析し、JSON形式で応答してください。
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        raw_response = self._query_llm(router_expert, messages)
        
        try:
            json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_response, re.DOTALL)
            if json_match:
                response_json_str = json_match.group(1)
            else:
                response_json_str = raw_response[raw_response.find('{'):raw_response.rfind('}')+1]

            data = json.loads(response_json_str)
            tool = data.get("tool", "no_tool")
            query = data.get("query")
            url = data.get("url")

            if tool not in ["wikipedia", "web_search", "complex_task", "no_tool"]:
                tool = "no_tool"

            return {"tool": tool, "query": query if query else prompt, "url": url}

        except (json.JSONDecodeError, AttributeError):
            response_lower = raw_response.lower()
            if "wikipedia" in response_lower:
                return {"tool": "wikipedia", "query": prompt, "url": None}
            if "web_search" in response_lower:
                return {"tool": "web_search", "query": prompt, "url": None}
            if "complex_task" in response_lower:
                return {"tool": "complex_task", "query": prompt, "url": None}
            return {"tool": "no_tool", "query": prompt, "url": None}

    def _find_router_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        """
        ルーティングタスクに最適なエキスパートを、優先順位とフォールバックを考慮して選択する。
        優先順位: Jamba > HRM > その他
        """
        candidates: Dict[str, ExpertModel] = {
            e.name.lower(): e for e in experts if e.chat_format != "diffusion"
        }
        
        if "jamba" in candidates:
            return candidates["jamba"]
        if "hrm" in candidates:
            return candidates["hrm"]
        
        if candidates:
            return list(candidates.values())[0]
        
        raise ValueError("利用可能なルーターエキスパートが見つかりません。")
