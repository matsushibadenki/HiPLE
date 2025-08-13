# path: ./domain/evaluation.py
# title: Expert Performance Metrics Schema
# description: Defines the data structure for tracking the performance of AI experts.

from dataclasses import dataclass, field

@dataclass
class PerformanceMetrics:
    """
    エキスパートのパフォーマンス指標を記録するデータクラス
    """
    success_count: int = 0
    failure_count: int = 0
    total_execution_time: float = 0.0
    # スコアは (成功数 / 総実行回数) * (1 - 正規化された平均実行時間) などで計算
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
        if self.success_count == 0:
            return 0.0
        return self.total_execution_time / self.success_count