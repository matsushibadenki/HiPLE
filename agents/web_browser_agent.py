# path: ./agents/web_browser_agent.py
# title: Web Browser Agent (LLM-Free Text Extractor)
# description: Extracts relevant text from HTML content without using an LLM, improving stability and focus.

from bs4 import BeautifulSoup, NavigableString
import re

class WebBrowserAgent:
    """
    Webページを解析し、クエリに関連するテキストコンテンツを抽出する。
    LLM呼び出しは行わず、テキスト処理に特化する。
    """
    def execute(self, content: str, query: str) -> str:
        """
        指定されたHTMLコンテンツから関連テキストを抽出する。
        """
        if "エラー:" in content:
            return content

        soup = BeautifulSoup(content, 'html.parser')
        # 不要なタグを削除
        for tag in soup(['script', 'style', 'nav', 'footer', 'aside', 'header', 'link', 'meta', 'form', 'button', 'input']):
            tag.decompose()
        
        # クエリに関連するキーワードでテキストを絞り込む
        keywords = re.split(r'\s+', query) + ["材料", "作り方", "レシピ", "手順", "ingredients", "instructions", "recipe"]
        
        relevant_texts = []
        # 全てのテキストノードを検索
        for element in soup.find_all(string=True):
            if isinstance(element, NavigableString):
                parent = element.parent
                # 親要素が存在し、表示されている要素のみを対象とする
                if parent and parent.name not in ['script', 'style', 'head', 'title']:
                    text_line = element.strip()
                    if text_line:
                        # キーワードが含まれているか、または親タグが意味的に重要かチェック
                        if any(keyword.lower() in text_line.lower() for keyword in keywords) or \
                           parent.name in ['h1', 'h2', 'h3', 'p', 'li', 'td']:
                            relevant_texts.append(text_line)
        
        if not relevant_texts:
            # 関連テキストが見つからない場合は、ボディ全体のテキストを返す
            body_text = soup.get_text(separator='\n', strip=True)
            if not body_text:
                return "エラー: ページからテキストコンテンツを抽出できませんでした。"
            final_text = body_text
        else:
            final_text = "\n".join(relevant_texts)
            
        # コンテキストウィンドウを考慮してテキストを切り詰める
        max_length = 8000
        return final_text[:max_length]