# path: ./services/tool_manager_service.py
# title: Tool Manager Service
# description: A centralized service for registering and executing available tools.

from typing import Dict, Any, List, cast
from agents.wikipedia_agent import WikipediaAgent
from agents.web_browser_agent import WebBrowserAgent
from services.web_browser_service import WebBrowserService
from domain.schemas import ExpertModel

class ToolManagerService:
    """
    システムで利用可能なツールを登録し、実行を管理するサービス。
    """
    def __init__(
        self,
        wikipedia_agent: WikipediaAgent,
        web_browser_agent: WebBrowserAgent,
        web_browser_service: WebBrowserService
    ):
        self.web_browser_service = web_browser_service
        self.tools: Dict[str, Any] = {
            "wikipedia_search": wikipedia_agent,
            "web_search": web_browser_agent,
        }
        print(f"🛠️ ToolManagerServiceが初期化され、{list(self.tools.keys())} が登録されました。")

    def get_tool_descriptions(self) -> str:
        """
        PlannerAgentのプロンプト用に、利用可能なツールの一覧と説明を文字列で返す。
        """
        return """- **wikipedia_search**: 普遍的で確立された知識（人物、場所、歴史的出来事、科学理論など）を調べる。
- **web_search**: 最新の情報、ニュース、トレンド、特定の製品レビューなど、時間と共に変化する情報を調べる。"""

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
                # URLが指定されている場合はそのページのコンテンツを取得し、そうでなければ検索（将来的な拡張）
                if not url:
                    return "エラー: Web検索にはURLの指定が必要です。"
                page_content = self.web_browser_service.get_page_content_sync(url)
                return cast(str, self.tools[tool_name].execute(page_content, query, experts))
            else:
                return f"エラー: ツール '{tool_name}' の実行ロジックが定義されていません。"
        except Exception as e:
            return f"エラー: ツール '{tool_name}' の実行中に問題が発生しました - {e}"

