# path: ./services/rag_manager_service.py
# title: RAG Manager Service
# description: Manages multiple retrievers and data sources for the RAG pipeline.

from typing import Dict, List, Iterator
from rag.data_sources import Document, DataSource
from rag.retrievers import BaseRetriever
from services.vectorization_service import VectorizationService

class RAGManagerService:
    """
    RAGパイプライン全体を管理するサービス。
    複数のリトリーバーを保持し、適切なリトリーバーを介して検索を実行する。
    """
    def __init__(self, vectorization_service: VectorizationService):
        self._retrievers: Dict[str, BaseRetriever] = {}
        self._vectorization_service = vectorization_service

    def register_retriever(self, name: str, retriever: BaseRetriever) -> None:
        """
        リトリーバーをマネージャーに登録する。
        """
        self._retrievers[name] = retriever
        print(f"🔍 RAGリトリーバー '{name}' を登録しました。")

    def build_index_from_source(self, retriever_name: str, data_source: DataSource) -> None:
        """
        指定されたデータソースからドキュメントを読み込み、指定されたリトリーバーのインデックスを構築する。
        """
        if retriever_name not in self._retrievers:
            raise ValueError(f"リトリーバー '{retriever_name}' は登録されていません。")
        
        documents = list(data_source.load_documents())
        retriever = self._retrievers[retriever_name]
        retriever.build_index(documents)

    def query(self, retriever_name: str, query_text: str, k: int = 3) -> List[Document]:
        """
        指定されたリトリーバーを使ってクエリを実行し、関連ドキュメントを取得する。
        """
        if retriever_name not in self._retrievers:
            raise ValueError(f"リトリーバー '{retriever_name}' は登録されていません。")
        
        retriever = self._retrievers[retriever_name]
        return retriever.retrieve(query_text, k=k)
