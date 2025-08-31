# path: ./services/web_browser_service.py
# title: Web Browser Service with Playwright
# description: Uses Playwright to robustly fetch and render web pages, including JavaScript-heavy sites.

import atexit
from typing import Optional
from playwright.sync_api import sync_playwright, Browser, Page, Playwright

class WebBrowserService:
    """
    Playwrightを使用してWebブラウジング機能を提供するサービス。
    """
    def __init__(self):
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None
        try:
            print("🔄 Playwrightを初期化しています...")
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=True)
            print("✅ Playwrightの初期化が完了しました。")
            # Ensure browser is closed on exit
            atexit.register(self.close_browser)
        except Exception as e:
            print(f"❌ Playwrightの初期化中にエラーが発生しました: {e}")
            print("ℹ️  コマンドプロンプトで 'playwright install' を実行して、ブラウザがインストールされているか確認してください。")
            self.playwright = None
            self.browser = None

    def get_page(self) -> Optional[Page]:
        """
        新しいブラウザページを取得または既存のものを再利用する。
        """
        if not self.browser:
            print("❌ ブラウザが初期化されていません。")
            return None
        try:
            # Use the first page if available, else create a new one.
            if self.browser.contexts and self.browser.contexts[0].pages:
                 return self.browser.contexts[0].pages[0]
            return self.browser.new_page()
        except Exception as e:
            print(f"❌ 新しいページの作成中にエラーが発生しました: {e}")
            return None

    def get_page_content(self, url: str) -> str:
        """
        指定されたURLのページコンテンツを取得する。
        """
        page = self.get_page()
        if not page:
            return "エラー: ブラウザページを取得できませんでした。"
        
        try:
            print(f"🖥️ ページに移動中: {url}")
            # DOMがロードされるまで待つ
            page.goto(url, timeout=30000, wait_until="domcontentloaded")
            
            # JavaScriptの非同期読み込みなどを考慮し、5秒間待機
            print("⏳ 動的コンテンツの読み込みを待機しています...")
            page.wait_for_timeout(5000)

            print("📝 ページコンテンツを取得中...")
            content = page.content()
            if not content:
                return f"エラー: URL '{url}' からコンテンツを取得できませんでした。"
            
            print(f"✅ コンテンツを正常に取得しました (長さ: {len(content)} 文字)。")
            return content

        except Exception as e:
            error_message = f"エラー: URL '{url}' の読み込み中に問題が発生しました - {e}"
            print(f"❌ {error_message}")
            return error_message

    def close_browser(self) -> None:
        """
        ブラウザとPlaywrightインスタンスを閉じる。
        """
        if self.browser or self.playwright:
            print("🖥️ ブラウザを終了しています...")
            if self.browser:
                self.browser.close()
                self.browser = None
            if self.playwright:
                self.playwright.stop()
                self.playwright = None
