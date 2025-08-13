# path: ./services/performance_tracker_service.py
# title: Performance Tracker Service
# description: AIエキスパートのパフォーマンスを追跡・評価し、最適なエキスパートを選択するサービス。

import time
from typing import Dict, Optional, List
from domain.evaluation import PerformanceMetrics
from domain.schemas import ExpertModel

class PerformanceTrackerService:
    """
    エキスパートのパフォーマンスを記録・管理するサービス
    """
    def __init__(self):
        self.performance_records: Dict[str, PerformanceMetrics] = {}

    def update_performance(
        self,
        expert_name: str,
        execution_time: float,
        success: bool
    ) -> None:
        """
        指定されたエキスパートのパフォーマンスを更新する
        """
        if expert_name not in self.performance_records:
            self.performance_records[expert_name] = PerformanceMetrics()

        record = self.performance_records[expert_name]
        if success:
            record.success_count += 1
            record.total_execution_time += execution_time
        else:
            record.failure_count += 1

        self._recalculate_score(expert_name)
        print(f"📊 Performance updated for '{expert_name}': Score={record.score:.2f}, SuccessRate={record.success_rate:.2f}, AvgTime={record.average_execution_time:.2f}s")


    def _recalculate_score(self, expert_name: str) -> None:
        """
        エキスパートのスコアを再計算する
        スコア = 成功率を重視しつつ、実行時間が短いほど高評価
        """
        record = self.performance_records.get(expert_name)
        if not record or record.total_runs == 0:
            return

        # 全エキスパートの平均実行時間を計算（スコア正規化のため）
        all_avg_times = [
            r.average_execution_time
            for r in self.performance_records.values()
            if r.success_count > 0
        ]
        max_avg_time = max(all_avg_times) if all_avg_times else 1.0
        
        # 実行時間ペナルティ (0から1の範囲、時間が長いほど1に近づく)
        # ゼロ除算を避ける
        normalized_time = record.average_execution_time / max_avg_time if max_avg_time > 0 else 0
        time_penalty = min(normalized_time, 1.0)

        # スコア計算（成功率を主軸に、実行時間が短いほどボーナス）
        record.score = record.success_rate * (1.0 - (time_penalty * 0.2))


    def get_best_expert(self, experts: List[ExpertModel], task_type: str = "general") -> Optional[ExpertModel]:
        """
        現在最もスコアの高い、利用可能なエキスパートを返す
        """
        best_expert: Optional[ExpertModel] = None
        highest_score = -1.0

        # 評価記録があるエキスパートのみを対象
        eligible_experts = [
            e for e in experts if e.name in self.performance_records and e.chat_format != "diffusion"
        ]

        if not eligible_experts:
            # 評価記録がない場合、デフォルト（HRMなど）を返す
            return next((e for e in experts if e.name.lower() == "hrm"), None)

        for expert in eligible_experts:
            score = self.performance_records[expert.name].score
            if score > highest_score:
                highest_score = score
                best_expert = expert
        
        # もし全エキスパートのスコアが0なら、ランダムやデフォルトにフォールバック
        if not best_expert:
             return next((e for e in experts if e.name.lower() == "hrm"), None)

        print(f"🏆 Best expert selected for '{task_type}': '{best_expert.name}' (Score: {highest_score:.2f})")
        return best_expert

    def get_performance_summary(self) -> str:
        """
        全エキスパートのパフォーマンスサマリーを文字列として返す
        """
        summary_lines = ["# Expert Performance Summary"]
        for name, record in sorted(self.performance_records.items(), key=lambda item: item[1].score, reverse=True):
            summary_lines.append(
                f"- **{name}**: "
                f"Score={record.score:.2f}, "
                f"SuccessRate={record.success_rate * 100:.1f}%, "
                f"AvgTime={record.average_execution_time:.2f}s, "
                f"Runs={record.total_runs}"
            )
        return "\n".join(summary_lines)