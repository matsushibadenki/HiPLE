# path: ./domain/schemas.py
# title: Data Schemas with Semantic Structure Vector
# description: 実行戦略に加え、意味構造ベクトル(SSV)を保持するフィールドをSubTaskに追加。

from dataclasses import dataclass, field
from typing import List, Optional, Any, Union, TYPE_CHECKING
from llama_cpp import Llama
import numpy as np

if TYPE_CHECKING:
    from diffusers import DiffusionPipeline

@dataclass
class ExpertModel:
    """
    各エキスパートモデルの設定と状態を管理するデータクラス
    """
    name: str
    description: str
    model_path: Optional[str]
    model_id: Optional[str]
    chat_format: str
    system_prompt: str
    execution_strategy: str = "inline" # "inline" or "worker"
    enabled: bool = False
    keywords: List[str] = field(default_factory=list)
    instance: Optional[Union[Llama, "DiffusionPipeline"]] = None
    is_loaded: bool = False

@dataclass
class SubTask:
    """
    分解されたサブタスクを管理するデータクラス
    """
    task_id: int
    description: str
    expert_name: str
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    ssv_description: str # 意味構造を記述した短いテキスト
    # ◾️◾️◾️◾️◾◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    dependencies: List[int] = field(default_factory=list)
    result: Optional[str] = None
    status: str = "pending"
    milestone_id: Optional[int] = None


@dataclass
class Milestone:
    """
    L2: 主要なマイルストーン（中間目標）を管理するデータクラス
    """
    milestone_id: int
    title: str
    description: str

@dataclass
class Plan:
    """
    実行計画全体を管理するデータクラス
    階層的な情報（L1, L2）と具体的なタスク（L3）を保持する
    """
    original_prompt: str
    overall_goal: str
    milestones: List[Milestone] = field(default_factory=list)
    tasks: List[SubTask] = field(default_factory=list)