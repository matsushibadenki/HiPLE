# path: ./rag/data_sources.py
# title: RAG Data Source Schemas and Interfaces
# description: Defines the standardized Document schema and the base class for all data sources.

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Iterator
from dataclasses import dataclass, field
from domain.schemas import Plan

@dataclass
class Document:
    """
    RAGシステム内で扱われる、分割されたテキスト情報の標準単位。
    """
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

class DataSource(ABC):
    """
    すべてのデータソースの基底クラスとなる抽象クラス。
    """
    @abstractmethod
    def load_documents(self) -> Iterator[Document]:
        """
        データソースからドキュメントを読み込み、イテレータとして返す。
        """
        pass

class PlanDataSource(DataSource):
    """
    HiPLEの実行計画(Plan)をデータソースとして扱うクラス。
    """
    def __init__(self, plan: Plan):
        self.plan = plan

    def load_documents(self) -> Iterator[Document]:
        """
        Planオブジェクトの各階層からDocumentを生成する。
        """
        # L1: Overall Goal
        yield Document(
            content=f"全体の目標: {self.plan.overall_goal}",
            metadata={"type": "L1_GOAL", "source": "plan"}
        )

        # L2: Milestones
        for m in self.plan.milestones:
            yield Document(
                content=f"マイルストーン「{m.title}」: {m.description}",
                metadata={"type": "L2_MILESTONE", "id": m.milestone_id, "source": "plan"}
            )
        
        # L3: Tasks
        for t in self.plan.tasks:
            yield Document(
                content=f"タスク {t.task_id} ({t.expert_name}): {t.description} (目的: {t.ssv_description})",
                metadata={"type": "L3_TASK", "id": t.task_id, "source": "plan"}
            )
