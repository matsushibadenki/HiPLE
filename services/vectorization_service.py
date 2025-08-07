# path: ./services/vectorization_service.py
# title: Vectorization Service
# description: テキストを意味ベクトル（Embedding）に変換するサービス。mypyエラー修正済み。

from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class VectorizationService:
    """
    テキストのベクトル化を担当するサービス。
    SentenceTransformerモデルを使用して、テキストを密なベクトル表現に変換します。
    """
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        サービスの初期化時に、指定されたモデルをロードします。
        
        Args:
            model_name (str): Hugging Face HubからロードするSentenceTransformerモデル名。
        """
        try:
            print(f"🔄 ベクトル化モデル '{model_name}' をロードしています...")
            self.model = SentenceTransformer(model_name)
            print("✅ ベクトル化モデルのロードが完了しました。")
        except Exception as e:
            print(f"❌ ベクトル化モデルのロードに失敗しました: {e}")
            raise

    def encode(self, text: str) -> np.ndarray:
        """
        単一のテキストをベクトルに変換します。
        
        Args:
            text (str): ベクトル化するテキスト。
        
        Returns:
            np.ndarray: 生成されたベクトル。
        """
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        return self.model.encode(text, convert_to_numpy=True)
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def encode_batch(self, texts: List[str]) -> np.ndarray:
        """
        テキストのリストをまとめてベクトルに変換します。
        
        Args:
            texts (List[str]): ベクトル化するテキストのリスト。
        
        Returns:
            np.ndarray: 生成されたベクトルのリスト。
        """
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        return self.model.encode(texts, convert_to_numpy=True)
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️