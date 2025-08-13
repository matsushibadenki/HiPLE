# path: ./rag/retrievers.py
# title: RAG Retriever Interfaces and Implementations
# description: Defines the retriever interface and a Faiss-based implementation for vector search.

from abc import ABC, abstractmethod
from typing import List, Optional
import numpy as np
import faiss
from rag.data_sources import Document
from services.vectorization_service import VectorizationService

class BaseRetriever(ABC):
    """
    すべてのリトリーバーの基底クラス。
    """
    @abstractmethod
    def build_index(self, documents: List[Document]) -> None:
        """
        ドキュメントのリストから検索インデックスを構築する。
        """
        pass

    @abstractmethod
    def retrieve(self, query: str, k: int = 3) -> List[Document]:
        """
        クエリに最も関連するドキュメントをk個検索する。
        """
        pass

class FaissRetriever(BaseRetriever):
    """
    FAISSを利用したベクトル検索リトリーバー。
    """
    def __init__(self, vectorization_service: VectorizationService):
        self.vector_service = vectorization_service
        self.index: Optional[faiss.IndexFlatL2] = None
        self.documents: List[Document] = []

    def build_index(self, documents: List[Document]) -> None:
        """
        ドキュメントをベクトル化し、FAISSインデックスを構築する。
        """
        print("🔄 FAISSインデックスを構築しています...")
        self.documents = documents
        
        if not self.documents:
            self.index = None
            print("🟡 ドキュメントが空のため、インデックスは構築されませんでした。")
            return

        contents = [doc.content for doc in self.documents]
        vectors = self.vector_service.encode_batch(contents)
        
        if vectors.size == 0:
            self.index = None
            print("🟡 ベクトルが生成されなかったため、インデックスは構築されませんでした。")
            return

        dimension = vectors.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(vectors)
        print(f"✅ FAISSインデックスの構築が完了しました。(次元数: {dimension}, データ数: {len(self.documents)})")

    def retrieve(self, query: str, k: int = 3) -> List[Document]:
        """
        クエリベクトルに意味的に近いドキュメントを検索する。
        """
        if self.index is None or not self.documents:
            return []

        query_vector = self.vector_service.encode(query).reshape(1, -1)
        distances, indices = self.index.search(query_vector, k)
        
        results = []
        for i in indices[0]:
            # 検索結果のインデックスがドキュメントリストの範囲内にあるか確認
            if 0 <= i < len(self.documents):
                results.append(self.documents[i])
        
        return results
