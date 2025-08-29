# path: ./services/performance_tracker_service.py
# title: Performance Tracker Service (with Robust Fallback)
# description: AIエキスパートのパフォーマンスをより正確に追跡・評価し、最適なエキスパートを選択するサービス。フォールバックロジックを強化。

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
        
        # 実行時間は成功・失敗に関わらず記録
        record.total_execution_time_all += execution_time
        
        if success:
            record.success_count += 1
            record.total_execution_time_on_success += execution_time
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
            if r.total_runs > 0
        ]
        
        # ゼロ除算と空リストのエラーを回避
        max_avg_time = max(all_avg_times) if all_avg_times else 1.0
        if max_avg_time == 0: max_avg_time = 1.0
        
        normalized_time = record.average_execution_time / max_avg_time
        time_penalty = min(normalized_time, 1.0)

        # スコア計算（成功率を主軸に、実行時間が短いほどボーナス）
        record.score = record.success_rate * (1.0 - (time_penalty * 0.2))


    def get_best_expert(self, experts: List[ExpertModel], task_type: str = "general") -> Optional[ExpertModel]:
        """
        現在最もスコアの高い、利用可能なエキスパートを返す。
        適切なエキスパートが見つからない場合は、安定したフォールバックを提供する。
        """
        best_expert: Optional[ExpertModel] = None
        highest_score = -1.0

        # 評価記録があるエキスパートのみを対象
        eligible_experts = [
            e for e in experts if e.name in self.performance_records and e.chat_format != "diffusion"
        ]

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # スコアが0より大きいエキスパートの中から最適解を探す
        for expert in eligible_experts:
            score = self.performance_records[expert.name].score
            if score > highest_score:
                highest_score = score
                best_expert = expert
        
        # スコアに基づく最適なエキスパートが見つかった場合はそれを返す
        if best_expert:
            print(f"🏆 Best expert selected for '{task_type}': '{best_expert.name}' (Score: {highest_score:.2f})")
            return best_expert

        # 適切なエキスパートが見つからない場合の、堅牢なフォールバック戦略
        print(f"🟡 No expert with a positive score for '{task_type}'. Using fallback strategy.")
        
        # 1. 思考の中心であるHRMを試す
        hrm_expert = next((e for e in experts if e.name.lower() == "hrm"), None)
        if hrm_expert:
            print("↪️ Fallback to default reasoner: 'HRM'")
            return hrm_expert
            
        # 2. 汎用的なJambaを試す
        jamba_expert = next((e for e in experts if e.name.lower() == "jamba"), None)
        if jamba_expert:
            print("↪️ Fallback to generalist: 'Jamba'")
            return jamba_expert

        # 3. それでも見つからない場合、最初のエキスパートを返す
        return next((e for e in experts if e.chat_format != "diffusion"), None)
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def get_performance_summary(self) -> str:
        """
        全エキスパートのパフォーマンスサマリーを文字列として返す
        """
        summary_lines = ["# Expert Performance Summary"]
        if not self.performance_records:
            return "# Expert Performance Summary\nNo performance records yet."
            
        for name, record in sorted(self.performance_records.items(), key=lambda item: item[1].score, reverse=True):
            summary_lines.append(
                f"- **{name}**: "
                f"Score={record.score:.2f}, "
                f"SuccessRate={record.success_rate * 100:.1f}%, "
                f"AvgTime={record.average_execution_time:.2f}s, "
                f"Runs={record.total_runs}"
            )
        return "\n".join(summary_lines)
