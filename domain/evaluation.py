# path: ./domain/evaluation.py
# title: Expert Performance Metrics Schema (Improved)
# description: Defines the data structure for tracking AI expert performance with more accurate time logging.

from dataclasses import dataclass, field

@dataclass
class PerformanceMetrics:
    """
    エキスパートのパフォーマンス指標を記録するデータクラス
    """
    success_count: int = 0
    failure_count: int = 0
    total_execution_time_on_success: float = 0.0
    total_execution_time_all: float = 0.0
    score: float = 0.0

    @property
    def total_runs(self) -> int:
        return self.success_count + self.failure_count

    @property
    def success_rate(self) -> float:
        if self.total_runs == 0:
            return 0.0
        return self.success_count / self.total_runs

    @property
    def average_execution_time(self) -> float:
        """全実行（成功・失敗問わず）の平均時間"""
        if self.total_runs == 0:
            return 0.0
        return self.total_execution_time_all / self.total_runs
