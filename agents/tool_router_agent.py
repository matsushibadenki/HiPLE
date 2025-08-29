# path: ./agents/tool_router_agent.py
# title: Tool Router Agent with Smarter Expert Selection
# description: ユーザーの要求を分析し、最適なツールを特定するエージェント。対話理解に優れたJambaを優先的に使用し、判断精度を向上させる。

import json
import re
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class ToolRouterAgent(BaseAgent):
    """
    ユーザーの要求を分析し、適切なツールと検索クエリを特定するインテリigentなルーター。
    """
    def execute(self, prompt: str, experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        プロンプトを分析し、ツール、検索クエリ、URLを含む辞書を返す。
        """
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        router_expert = self._find_router_expert(experts)
        print(f"🧠 Router expert selected: {router_expert.name}")
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        system_prompt = """あなたはユーザーの要求を分析し、その要求を達成するために最も適したツールと、そのツールで検索すべきキーワードを判断する、優秀なディスパッチャーです。
以下のJSONフォーマットで、判断結果のみを答えてください。余計な説明は一切不要です。

# 出力フォーマット
```json
{
  "tool": "（'wikipedia', 'web_search', 'complex_task', 'no_tool' のいずれか）",
  "query": "（ツールを使用する場合に検索すべきキーワード。ツール不要の場合はnull）",
  "url": "（web_searchの場合にアクセスすべきURL。それ以外はnull）"
}
```

# 判断基準と具体例
- `wikipedia`: **特定の固有名詞、専門用語、歴史上の出来事**など、百科事典的な知識が求められている場合。
    - 例1: ユーザー要求「徳川家康について教えて」 -> {"tool": "wikipedia", "query": "徳川家康", "url": null}
    - 例2: ユーザー要求「量子もつれのメカニズムを知りたい」 -> {"tool": "wikipedia", "query": "量子もつれ", "url": null}
    - 例3: ユーザー要求「エッフェル塔はどこにありますか？」 -> {"tool": "wikipedia", "query": "エッフェル塔", "url": null}

- `web_search`: **最新のニュース、トレンド、製品レビュー、特定のURLの要約**など、リアルタイム性や網羅性が重要な情報が求められている場合。
    - 例1: ユーザー要求「今日の東京の天気は？」 -> {"tool": "web_search", "query": "東京 天気", "url": null}
    - 例2: ユーザー要求「この記事(https://example.com/news)を要約して」 -> {"tool": "web_search", "query": "記事の要約", "url": "https://example.com/news"}

- `complex_task`: **コード生成、画像作成、複数ステップの指示、創造的な文章執筆**など、単一の検索では完結しないタスクの場合。
    - 例1: ユーザー要求「Pythonで簡単なWebサーバーを実装して」 -> {"tool": "complex_task", "query": null, "url": null}
    - 例2: ユーザー要求「猫がマフィアのスーツを着ている画像を作って」 -> {"tool": "complex_task", "query": null, "url": null}

- `no_tool`: **一般的な挨拶や単純な対話**の場合。
    - 例1: ユーザー要求「こんにちは」 -> {"tool": "no_tool", "query": null, "url": null}
    - 例2: ユーザー要求「ありがとう」 -> {"tool": "no_tool", "query": null, "url": null}

ユーザーの要求を慎重に読み、上記のJSON形式で応答してください。
"""

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

    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    def _find_router_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        """
        ルーティングタスクに最適なエキスパートを、優先順位とフォールバックを考慮して選択する。
        優先順位: Jamba > HRM > その他
        """
        # 拡散モデルを除外した候補リストを作成
        candidates: Dict[str, ExpertModel] = {
            e.name.lower(): e for e in experts if e.chat_format != "diffusion"
        }
        
        # 優先順位に従ってエキスパートを選択
        if "jamba" in candidates:
            return candidates["jamba"]
        if "hrm" in candidates:
            return candidates["hrm"]
        
        # 上記が見つからない場合、利用可能な最初のエキスパートを返す
        if candidates:
            return list(candidates.values())[0]
        
        raise ValueError("利用可能なルーターエキスパートが見つかりません。")
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
