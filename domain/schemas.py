# path: ./domain/schemas.py
# title: Data Schemas with Self-Evaluation Field
# description: SubTaskに自己評価（自信度と理由）を記録するフィールドを追加。

from dataclasses import dataclass, field
from typing import List, Optional, Any, Union, Dict, TYPE_CHECKING
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
    cost_score: int = 5  # コスト評価 (1: low, 10: high)
    speed_score: int = 5 # 速度評価 (1: slow, 10: fast)
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
    ssv_description: str # 意味構造を記述した短いテキスト
    consultation_experts: List[str] = field(default_factory=list) # 相談相手のエキスパート名リスト
    reviewer_expert: Optional[str] = None # レビュー担当のエキスパート名
    feedback_history: List[Dict[str, str]] = field(default_factory=list) # レビューと修正の履歴
    dependencies: List[int] = field(default_factory=list)
    result: Optional[str] = None
    status: str = "pending"
    milestone_id: Optional[int] = None
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    self_evaluation: Optional[Dict[str, Any]] = None # 自己評価（自信度、理由など）
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️


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
