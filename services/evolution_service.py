# path: ./services/evolution_service.py
# title: Self-Evolution Service
# description: Manages the self-evolution loop based on performance metrics and safety constraints.

from typing import Dict, Any, Optional, List
from services.performance_tracker_service import PerformanceTrackerService
from domain.boundary_enforcer import BoundaryConditionEnforcer
from domain.schemas import ExpertModel

class EvolutionService:
    """
    エキスパートのパフォーマンスに基づき、システムの自己進化を管理するサービス。
    """
    def __init__(
        self,
        performance_tracker: PerformanceTrackerService,
        boundary_enforcer: BoundaryConditionEnforcer,
        all_experts: List[ExpertModel]
    ):
        self.performance_tracker = performance_tracker
        self.boundary_enforcer = boundary_enforcer
        self.all_experts = {expert.name.lower(): expert for expert in all_experts}
        # 進化の提案をセッション内で一度だけ行うためのフラグ
        self.evolution_proposed_this_session: Dict[str, bool] = {}

    def run_evolution_cycle(self) -> Optional[str]:
        """
        進化サイクルを実行し、改善提案があれば文字列として返す。
        """
        # 1. パフォーマンスが低いエキスパートを特定
        underperforming_experts = self.performance_tracker.get_underperforming_experts()
        if not underperforming_experts:
            return None

        # 2. 改善策を提案
        for expert_name, metrics in underperforming_experts:
            if self.evolution_proposed_this_session.get(expert_name):
                continue # このセッションでは既に提案済み

            # 今は「無効化」のみを提案する
            proposed_change = {
                "action": "disable",
                "expert_name": expert_name,
                "reason": f"Success rate is {metrics.success_rate:.2%} over {metrics.total_runs} runs."
            }

            # 3. 境界条件エンフォーサーによる検証
            is_valid, message = self.boundary_enforcer.validate_evolution(proposed_change)

            if is_valid:
                print(f"🧬 Evolution Proposal: {message}")
                self.evolution_proposed_this_session[expert_name] = True
                
                # 提案を返す (実際のファイル書き込みは行わない)
                evolution_summary = (
                    f"**[SELF-EVOLUTION PROPOSAL]**\n"
                    f"- **Action:** Disable expert '{expert_name}'.\n"
                    f"- **Reason:** Low performance detected (Success Rate: {metrics.success_rate:.2%}).\n"
                    f"- **Suggestion:** Consider setting `enabled: false` for this expert in `config/models.yml` to improve overall system performance."
                )
                return evolution_summary
            else:
                print(f"🧬 Evolution Proposal for '{expert_name}' was rejected. Reason: {message}")
                # 却下された提案も記録し、再提案しないようにする
                self.evolution_proposed_this_session[expert_name] = True

        return None
