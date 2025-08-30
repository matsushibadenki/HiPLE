# path: ./agents/metacognition_agent.py
# title: Metacognition Agent
# description: Analyzes the cognitive load of a plan to prevent overly complex or inefficient execution.

from typing import List, Dict, Any, Tuple
from domain.schemas import Plan

class MetacognitionAgent:
    """
    計画の複雑性やリソース消費を予測し、実行前に評価するメタ認知エージェント。
    """
    def __init__(self, task_limit: int = 20, dependency_depth_limit: int = 5):
        self.task_limit = task_limit
        self.dependency_depth_limit = dependency_depth_limit

    def analyze_cognitive_load(self, plan: Plan) -> Tuple[bool, str]:
        """
        計画の認知負荷を分析する。

        Returns:
            Tuple[bool, str]: (実行可能か, 分析メッセージ)
        """
        # 1. タスク数のチェック
        if len(plan.tasks) > self.task_limit:
            return False, f"Cognitive Overload: The plan exceeds the maximum task limit of {self.task_limit}."

        # 2. 依存関係の深さをチェック
        max_depth, path = self._calculate_max_dependency_depth(plan)
        if max_depth > self.dependency_depth_limit:
            path_str = " -> ".join(map(str, path))
            return False, f"Cognitive Overload: The plan's dependency depth ({max_depth}) exceeds the limit of {self.dependency_depth_limit}. Path: {path_str}"

        return True, "Cognitive load analysis passed."

    def _calculate_max_dependency_depth(self, plan: Plan) -> Tuple[int, List[int]]:
        """計画の依存関係の最大の深さを計算する"""
        if not plan.tasks:
            return 0, []

        memo: Dict[int, Tuple[int, List[int]]] = {}
        task_map = {task.task_id: task for task in plan.tasks}
        max_depth = 0
        longest_path: List[int] = []

        def dfs(task_id: int) -> Tuple[int, List[int]]:
            if task_id in memo:
                return memo[task_id]
            
            task = task_map.get(task_id)
            if not task or not task.dependencies:
                memo[task_id] = (1, [task_id])
                return 1, [task_id]

            max_child_depth = 0
            best_path: List[int] = []
            for dep_id in task.dependencies:
                depth, path = dfs(dep_id)
                if depth > max_child_depth:
                    max_child_depth = depth
                    best_path = path
            
            current_depth = max_child_depth + 1
            current_path = best_path + [task_id]
            memo[task_id] = (current_depth, current_path)
            return current_depth, current_path

        for task in plan.tasks:
            depth, path = dfs(task.task_id)
            if depth > max_depth:
                max_depth = depth
                longest_path = path
        
        return max_depth, longest_path