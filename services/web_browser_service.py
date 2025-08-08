# path: ./services/web_browser_service.py
# title: Web Browser Service
# description: Playwrightを使用してヘッドレスブラウザを制御し、Webページのコンテンツを取得するサービス。

import asyncio
from typing import Optional
from playwright.async_api import async_playwright, Browser, Page

class WebBrowserService:
    """
    Playwrightをラップして、非同期的なブラウザ操作を提供するサービス。
    """
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.browser: Optional[Browser] = None

    async def launch_browser(self) -> None:
        """ブラウザを起動する"""
        if self.browser and self.browser.is_connected():
            return
        p = await async_playwright().start()
        self.browser = await p.chromium.launch(headless=self.headless)
        print("🖥️ ブラウザを起動しました。")

    async def close_browser(self) -> None:
        """ブラウザを閉じる"""
        if self.browser:
            await self.browser.close()
            self.browser = None
            print("🖥️ ブラウザを終了しました。")

    async def get_page_content(self, url: str) -> str:
        """
        指定されたURLのレンダリング済みHTMLコンテンツを取得する。

        Args:
            url (str): 調査対象のURL。

        Returns:
            str: レンダリング後のHTMLコンテンツ。
        """
        if not self.browser:
            await self.launch_browser()
        
        page: Optional[Page] = None
        try:
            page = await self.browser.new_page()
            print(f"📄 ページにアクセスしています: {url}")
            await page.goto(url, wait_until="networkidle", timeout=60000)
            content = await page.content()
            print(f"✅ コンテンツの取得に成功しました。(文字数: {len(content)})")
            return content
        except Exception as e:
            print(f"❌ ページのコンテンツ取得に失敗しました: {e}")
            return f"エラー: {url} のコンテンツ取得に失敗しました。理由: {e}"
        finally:
            if page:
                await page.close()

# 非同期処理の同期的な呼び出しラッパー（テストや同期的なエージェントからの利用を想定）
def run_async_get_page_content(url: str) -> str:
    service = WebBrowserService()
    try:
        content = asyncio.run(service.get_page_content(url))
    finally:
        asyncio.run(service.close_browser())
    return content

if __name__ == '__main__':
    # テスト実行
    test_url = "https://www.google.com/search?q=AI+news"
    page_html = run_async_get_page_content(test_url)
    print("\n--- 取得したHTML（先頭500文字） ---")
    print(page_html[:500])