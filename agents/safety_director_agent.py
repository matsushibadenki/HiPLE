# path: ./agents/safety_director_agent.py
# title: Safety Director Agent with Confidence Check (Completed)
# description: システムの健全性に加え、各タスクの自己評価（自信度）を監視し、低品質な成果物を検知する。

from typing import List, Dict, Any, Optional
from domain.schemas import Plan, SubTask
from workspace.global_workspace import GlobalWorkspace

class SafetyDirectorAgent:
    """
    システム全体の思考プロセスを監視し、非効率なループや矛盾、
    リスク（低自信度の応答など）を検知して介入する安全監督官エージェント。
    """
    def __init__(self, max_replanning: int = 3, max_feedback_loops: int = 3, confidence_threshold: float = 0.6):
        self.max_replanning = max_replanning
        self.max_feedback_loops = max_feedback_loops
        self.confidence_threshold = confidence_threshold

    def review_thought_process(self, workspace: GlobalWorkspace) -> Optional[str]:
        """
        現在の思考プロセスをレビューし、問題があれば介入指示を返す。
        """
        thought_process = workspace.thought_process

        # 1. 無限再計画ループの検知
        planning_attempts = sum(1 for thought in thought_process if thought.get("type") == "planning_start")
        if planning_attempts > self.max_replanning:
            return f"Safety Alert: Planning has failed {planning_attempts} times. Aborting task to prevent infinite loop."

        # 2. 特定タスクでの無限フィードバックループの検知
        feedback_counts: Dict[int, int] = {}
        for thought in thought_process:
            if thought.get("type") == "review_start":
                task_id = thought.get("content", {}).get("task_id")
                if task_id:
                    feedback_counts[task_id] = feedback_counts.get(task_id, 0) + 1
                    if feedback_counts[task_id] > self.max_feedback_loops:
                        return f"Safety Alert: Task {task_id} is stuck in a feedback loop. Aborting."

        # 3. 低自信度タスクの検知
        for thought in thought_process:
            if thought.get("type") == "task_completed":
                content = thought.get("content", {})
                evaluation = content.get("self_evaluation")
                if evaluation and isinstance(evaluation, dict):
                    confidence = evaluation.get("confidence", 1.0)
                    if isinstance(confidence, (int, float)) and confidence < self.confidence_threshold:
                        task_id = content.get("task_id")
                        reasoning = evaluation.get("reasoning", "No reason provided.")
                        # 重要度が低い警告として返し、処理は続行させる
                        print(f"⚠️ Safety Warning: Task {task_id} completed with low confidence ({confidence:.2f}). Reason: {reasoning}")

        return None
