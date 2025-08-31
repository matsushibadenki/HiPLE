# path: ./services/web_browser_service.py
# title: Web Browser Service (Synchronous Implementation)
# description: Playwrightを使用してヘッドレスブラウザを制御し、Webページのコンテンツを取得するサービス。非同期処理に起因するエラーを解消するため、同期APIを使用。

from typing import Optional
from playwright.sync_api import sync_playwright, Browser, Page, Playwright

class WebBrowserService:
    """
    Playwrightをラップして、同期的なブラウザ操作を提供するサービス。
    """
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None

    def launch_browser(self) -> None:
        """ブラウザを起動する"""
        if self.browser and self.browser.is_connected:
            return
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        print("🖥️ ブラウザを起動しました。")

    def close_browser(self) -> None:
        """ブラウザを閉じる"""
        if self.browser:
            self.browser.close()
            self.browser = None
        if self.playwright:
            self.playwright.stop()
            self.playwright = None
        print("🖥️ ブラウザを終了しました。")

    def get_page_content(self, url: str) -> str:
        """
        指定されたURLのレンダリング済みHTMLコンテンツを取得する。
        """
        if not self.browser or not self.browser.is_connected:
            self.launch_browser()
        
        page: Optional[Page] = None
        try:
            # self.browserがNoneでないことをアサーションで確認
            assert self.browser is not None
            page = self.browser.new_page()
            print(f"📄 ページにアクセスしています: {url}")
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            content = page.content()
            print(f"✅ コンテンツの取得に成功しました。(文字数: {len(content)})")
            return content
        except Exception as e:
            print(f"❌ ページのコンテンツ取得に失敗しました: {e}")
            return f"エラー: {url} のコンテンツ取得に失敗しました。理由: {e}"
        finally:
            if page:
                page.close()