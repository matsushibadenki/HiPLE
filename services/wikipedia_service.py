# path: ./services/wikipedia_service.py
# title: Wikipedia Service (mypy compatible)
# description: Wikipedia APIをラップし、記事の検索や要約の取得を行うサービス。mypyエラーを修正。

import wikipedia
from typing import List, Optional, cast

class WikipediaService:
    """
    Wikipediaライブラリをラップして、言語設定やエラーハンドリングを行うサービス。
    """
    def __init__(self, lang: str = "ja"):
        """
        サービスの初期化時に、検索言語を設定します。
        """
        try:
            wikipedia.set_lang(lang)
            self.lang = lang
            print(f"🌍 Wikipediaの検索言語を '{lang}' に設定しました。")
        except Exception as e:
            print(f"⚠️ Wikipediaの言語設定に失敗しました: {e}。デフォルトの'en'を使用します。")
            wikipedia.set_lang("en")
            self.lang = "en"

    def search(self, query: str, results: int = 3) -> Optional[List[str]]:
        """
        指定されたクエリでWikipediaの記事を検索し、候補のタイトルリストを返す。

        Args:
            query (str): 検索クエリ。
            results (int): 取得する候補の数。

        Returns:
            Optional[List[str]]: 記事タイトルのリスト。見つからない場合はNone。
        """
        try:
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            search_results = wikipedia.search(query, results=results)
            if not search_results:
                return None
            # mypyに正しい型を伝えるためにキャストする
            return cast(List[str], search_results)
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        except Exception as e:
            print(f"❌ Wikipediaでの検索中にエラーが発生しました: {e}")
            return None

    def get_summary(self, title: str, sentences: int = 5) -> Optional[str]:
        """
        指定されたタイトルの記事の要約を取得する。

        Args:
            title (str): 記事の正式タイトル。
            sentences (int): 要約の文の数。

        Returns:
            Optional[str]: 記事の要約。見つからない、または曖昧な場合はNone。
        """
        try:
            # auto_suggest=Falseで厳密なタイトルマッチを行う
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            summary = wikipedia.summary(title, sentences=sentences, auto_suggest=False)
            return cast(str, summary)
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        except wikipedia.exceptions.PageError:
            print(f"🟡 記事 '{title}' が見つかりませんでした。")
            return None
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"🟡 記事名 '{title}' は曖昧です。候補: {e.options[:3]}")
            # 最も可能性の高い候補で再試行
            try:
                first_option = e.options[0]
                print(f"↪️ 最初の候補 '{first_option}' で再試行します。")
                # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
                summary = wikipedia.summary(first_option, sentences=sentences, auto_suggest=False)
                return cast(str, summary)
                # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            except Exception as inner_e:
                print(f"❌ 再試行中にエラーが発生しました: {inner_e}")
                return None
        except Exception as e:
            print(f"❌ 記事の要約取得中にエラーが発生しました: {e}")
            return None
