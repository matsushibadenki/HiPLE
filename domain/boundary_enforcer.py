# path: ./domain/boundary_enforcer.py
# title: Boundary Condition Enforcer
# description: Enforces safety constraints on the self-evolution process.

from typing import Dict, Any, Tuple, List

class BoundaryConditionEnforcer:
    """
    自己進化プロセスが安全な境界内で行われることを保証するクラス。
    """
    def __init__(self):
        # システムの機能に不可欠な、無効化してはならないエキスパートのリスト
        self.protected_experts: List[str] = ["hrm", "reporter", "greeter"]

    def validate_evolution(self, proposed_change: Dict[str, Any]) -> Tuple[bool, str]:
        """
        提案された構成変更を検証する。

        Args:
            proposed_change (Dict[str, Any]): e.g., {"action": "disable", "expert_name": "Jamba"}

        Returns:
            Tuple[bool, str]: (検証が通ったか, メッセージ)
        """
        action = proposed_change.get("action")
        expert_name = proposed_change.get("expert_name")

        if not action or not expert_name:
            return False, "Invalid change proposal: 'action' and 'expert_name' are required."

        if action == "disable":
            if expert_name.lower() in self.protected_experts:
                return False, f"Validation failed: Core expert '{expert_name}' cannot be disabled."

        # 今後、コストや速度スコアの急激な変更を制限するルールなどを追加できる
        
        return True, "Proposed change is within safe boundaries."
