# path: ./services/retrieval_service.py
# title: Hierarchical Retrieval Service
# description: 階層化された計画の各要素をベクトル化し、意味検索可能にするRAGサービス。

from typing import List, Dict, Any, Optional, Tuple
import numpy as np
import faiss
from domain.schemas import Plan
from services.vectorization_service import VectorizationService

class RetrievalService:
    """
    階層化された計画をベクトルDBに格納し、
    関連性の高いコンテキストを検索するRAGサービス。
    """
    def __init__(self, vectorization_service: VectorizationService):
        self.vector_service = vectorization_service
        self.index: Optional[faiss.IndexFlatL2] = None
        self.metadata: List[Dict[str, Any]] = []

    def build_index(self, plan: Plan) -> None:
        """
        計画の各階層（Goal, Milestone, Task）からインデックスを構築する。
        """
        print("🔄 階層的計画のベクトルインデックスを構築しています...")
        self.metadata = []
        all_texts: List[str] = []

        # L1: Overall Goal
        self.metadata.append({"type": "L1_GOAL", "content": plan.overall_goal})
        all_texts.append(f"全体の目標: {plan.overall_goal}")

        # L2: Milestones
        for m in plan.milestones:
            self.metadata.append({"type": "L2_MILESTONE", "id": m.milestone_id, "content": m.description})
            all_texts.append(f"マイルストーン「{m.title}」: {m.description}")
        
        # L3: Tasks
        for t in plan.tasks:
            self.metadata.append({"type": "L3_TASK", "id": t.task_id, "content": t.description})
            all_texts.append(f"タスク {t.task_id}: {t.description}")

        if not all_texts:
            self.index = None
            print("🟡 テキストが空のため、インデックスは構築されませんでした。")
            return

        vectors = self.vector_service.encode_batch(all_texts)
        dimension = vectors.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(vectors)
        print(f"✅ ベクトルインデックスの構築が完了しました。(次元数: {dimension}, データ数: {len(all_texts)})")

    def search(self, query: str, k: int = 3) -> List[Dict[str, Any]]:
        """
        クエリベクトルに意味的に近い計画要素を検索する。
        """
        if not self.index or not self.metadata:
            return []

        query_vector = self.vector_service.encode(query).reshape(1, -1)
        distances, indices = self.index.search(query_vector, k)
        
        results = []
        for i in indices[0]:
            if i < len(self.metadata):
                results.append(self.metadata[i])
        
        return results