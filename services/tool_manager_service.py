# path: ./services/tool_manager_service.py
# title: Tool Manager Service
# description: A centralized service for registering and executing available tools.

from typing import Dict, Any, List, cast
from agents.wikipedia_agent import WikipediaAgent
from services.web_browser_service import WebBrowserService
from domain.schemas import ExpertModel
import googlesearch

class ToolManagerService:
    """
    システムで利用可能なツールを登録し、実行を管理するサービス。
    """
    def __init__(
        self,
        wikipedia_agent: WikipediaAgent,
        web_browser_service: WebBrowserService
    ):
        self.web_browser_service = web_browser_service
        self.tools: Dict[str, Any] = {
            "wikipedia_search": wikipedia_agent,
            "web_search": self.web_browser_service,
        }
        print(f"🛠️ ToolManagerServiceが初期化され、{list(self.tools.keys())} が登録されました。")

    def get_tool_descriptions(self) -> str:
        """
        PlannerAgentのプロンプト用に、利用可能なツールの一覧と説明を文字列で返す。
        """
        return """- **wikipedia_search**: 普遍的で確立された知識（人物、場所、歴史的出来事、科学理論など）を調べる。
- **web_search**: 最新の情報、ニュース、トレンド、特定の製品レビュー、レシピなど、時間と共に変化する情報を調べる。"""

    def execute_tool(self, tool_name: str, query: str, url: str, experts: List[ExpertModel]) -> str:
        """
        指定されたツールを実行する。
        """
        if tool_name not in self.tools:
            return f"エラー: 不明なツール '{tool_name}' が指定されました。"

        print(f"🔧 ツール '{tool_name}' を実行します。Query: '{query}'")
        try:
            if tool_name == "wikipedia_search":
                return cast(str, self.tools[tool_name].execute(query, experts))
            elif tool_name == "web_search":
                if not url:
                    print(f"🔍 URLが指定されていないため、Googleで '{query}' を検索します...")
                    try:
                        search_results = list(googlesearch.search(query, num=1, stop=1, pause=2))
                        if not search_results:
                            return f"エラー: '{query}' に関連するWebページが見つかりませんでした。"
                        url = search_results[0]
                        print(f"🔗 最初の検索結果を使用します: {url}")
                    except Exception as e:
                        return f"エラー: Google検索中にエラーが発生しました - {e}"
                
                # エージェントを介さず、Webブラウザサービスから直接コンテンツを返す
                return self.tools[tool_name].get_page_content(url)
            else:
                return f"エラー: ツール '{tool_name}' の実行ロジックが定義されていません。"
        except Exception as e:
            return f"エラー: ツール '{tool_name}' の実行中に問題が発生しました - {e}"