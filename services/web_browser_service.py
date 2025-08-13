# path: ./services/web_browser_service.py
# title: Web Browser Service
# description: Playwrightを使用してヘッドレスブラウザを制御し、Webページのコンテンツを取得するサービス。

import asyncio
from typing import Optional
from playwright.async_api import async_playwright, Browser, Page, Playwright

class WebBrowserService:
    """
    Playwrightをラップして、非同期的なブラウザ操作を提供するサービス。
    """
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None

    async def launch_browser(self) -> None:
        """ブラウザを起動する"""
        if self.browser and self.browser.is_connected():
            return
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=self.headless)
        print("🖥️ ブラウザを起動しました。")

    async def close_browser(self) -> None:
        """ブラウザを閉じる"""
        if self.browser:
            await self.browser.close()
            self.browser = None
        if self.playwright:
            await self.playwright.stop()
            self.playwright = None
        print("🖥️ ブラウザを終了しました。")

    async def get_page_content(self, url: str) -> str:
        """
        指定されたURLのレンダリング済みHTMLコンテンツを取得する。
        """
        if not self.browser or not self.browser.is_connected():
            await self.launch_browser()
        
        page: Optional[Page] = None
        try:
            # self.browserがNoneでないことをアサーションで確認
            assert self.browser is not None
            page = await self.browser.new_page()
            print(f"📄 ページにアクセスしています: {url}")
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            content = await page.content()
            print(f"✅ コンテンツの取得に成功しました。(文字数: {len(content)})")
            return content
        except Exception as e:
            print(f"❌ ページのコンテンツ取得に失敗しました: {e}")
            return f"エラー: {url} のコンテンツ取得に失敗しました。理由: {e}"
        finally:
            if page:
                await page.close()
