# path: ./agents/safety_director_agent.py
# title: Safety Director Agent
# description: Monitors the overall system health and thought process to ensure safe and efficient operation.

from typing import List, Dict, Any, Optional
from domain.schemas import Plan, SubTask
from workspace.global_workspace import GlobalWorkspace

class SafetyDirectorAgent:
    """
    システム全体の思考プロセスを監視し、非効率なループや矛盾、
    リスクを検知して介入する安全監督官エージェント。
    """
    def __init__(self, max_replanning: int = 3, max_feedback_loops: int = 3):
        self.max_replanning = max_replanning
        self.max_feedback_loops = max_feedback_loops

    def review_thought_process(self, workspace: GlobalWorkspace) -> Optional[str]:
        """
        現在の思考プロセスをレビューし、問題があれば介入指示を返す。

        Returns:
            Optional[str]: 問題がある場合は停止や再計画を促すエラーメッセージ、問題なければNone。
        """
        thought_process = workspace.thought_process

        # 1. 無限再計画ループの検知
        planning_attempts = sum(1 for thought in thought_process if thought.get("type") == "planning_start")
        if planning_attempts > self.max_replanning:
            return f"Error: Planning has failed {planning_attempts} times. Aborting task to prevent infinite loop."

        # 2. 特定タスクでの無限フィードバックループの検知
        feedback_counts: Dict[int, int] = {}
        for thought in thought_process:
            if thought.get("type") == "review_start":
                task_id = thought.get("content", {}).get("task_id")
                if task_id:
                    feedback_counts[task_id] = feedback_counts.get(task_id, 0) + 1
                    if feedback_counts[task_id] > self.max_feedback_loops:
                        return f"Error: Task {task_id} is stuck in a feedback loop. Aborting."

        # 今後、価値観整合性チェックなどのロジックをここに追加できる

        return None