# path: ./services/plan_evaluation_service.py
# title: Plan Evaluation Service
# description: 計画の意味的一貫性をベクトル空間で評価するサービス。

from typing import List, Tuple
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from services.vectorization_service import VectorizationService
from domain.schemas import SubTask

class PlanEvaluationService:
    """
    計画の意味的な妥当性を評価するサービス。
    """
    def __init__(self, vectorization_service: VectorizationService):
        self.vector_service = vectorization_service

    def check_semantic_coherence(
        self,
        tasks: List[SubTask],
        threshold: float = 0.5
    ) -> Tuple[bool, str]:
        """
        計画のステップ間の意味的な一貫性を検証する。
        連続するタスクのSSV（意味構造ベクトル）間のコサイン類似度が
        しきい値を下回った場合に警告する。

        Args:
            tasks (List[SubTask]): 評価対象のタスクリスト。
            threshold (float): 一貫性の警告を出すコサイン類似度のしきい値。

        Returns:
            Tuple[bool, str]: (一貫性が保たれているか, 評価メッセージ)
        """
        if len(tasks) <= 1:
            return True, "計画は単一ステップのため、一貫性チェックは不要です。"

        # SSV記述からベクトルを一括生成
        ssv_descriptions = [task.ssv_description for task in tasks]
        ssv_vectors = self.vector_service.encode_batch(ssv_descriptions)

        coherence_issues = []
        # 実行順にタスクをソート
        sorted_tasks = sorted(tasks, key=lambda t: t.task_id)
        
        for i in range(len(sorted_tasks) - 1):
            # 隣接するタスクのベクトルを取得
            vec1 = ssv_vectors[i].reshape(1, -1)
            vec2 = ssv_vectors[i+1].reshape(1, -1)
            similarity = cosine_similarity(vec1, vec2)[0][0]

            if similarity < threshold:
                issue = (
                    f"ステップ {i+1} から {i+2} への意味的な飛躍が検出されました (類似度: {similarity:.2f})。\n"
                    f"  - Step {i+1}: '{sorted_tasks[i].description}' (SSV: {sorted_tasks[i].ssv_description})\n"
                    f"  - Step {i+2}: '{sorted_tasks[i+1].description}' (SSV: {sorted_tasks[i+1].ssv_description})\n"
                    "これらのタスク間の関連性が低い可能性があります。計画を見直してください。"
                )
                coherence_issues.append(issue)

        if coherence_issues:
            error_message = "計画の意味的一貫性に問題があります:\n" + "\n".join(coherence_issues)
            return False, error_message

        return True, "計画は意味的に一貫しています。"