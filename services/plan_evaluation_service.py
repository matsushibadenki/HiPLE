# path: ./services/plan_evaluation_service.py
# title: Plan Evaluation Service
# description: 計画の意味的一貫性をベクトル空間で評価するサービス。

from typing import List, Tuple
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class PlanEvaluationService:
    """
    計画の意味的な妥当性を評価するサービス。
    """
    def check_semantic_coherence(
        self, 
        task_descriptions: List[str],
        ssv_vectors: np.ndarray, 
        threshold: float = 0.5
    ) -> Tuple[bool, str]:
        """
        計画のステップ間の意味的な一貫性を検証する。
        連続するタスク間のコサイン類似度がしきい値を下回った場合に警告する。

        Args:
            task_descriptions (List[str]): タスクの説明テキストのリスト。
            ssv_vectors (np.ndarray): タスクに対応する意味構造ベクトル(SSV)のリスト。
            threshold (float): 一貫性の警告を出すコサイン類似度のしきい値。

        Returns:
            Tuple[bool, str]: (一貫性が保たれているか, 評価メッセージ)
        """
        if len(ssv_vectors) <= 1:
            return True, "計画は単一ステップのため、一貫性チェックは不要です。"

        coherence_issues = []
        for i in range(len(ssv_vectors) - 1):
            # 隣接するベクトルのコサイン類似度を計算
            vec1 = ssv_vectors[i].reshape(1, -1)
            vec2 = ssv_vectors[i+1].reshape(1, -1)
            similarity = cosine_similarity(vec1, vec2)[0][0]

            if similarity < threshold:
                issue = (
                    f"ステップ {i+1} から {i+2} への意味的な飛躍が検出されました (類似度: {similarity:.2f})。\n"
                    f"  - Step {i+1}: '{task_descriptions[i]}'\n"
                    f"  - Step {i+2}: '{task_descriptions[i+1]}'\n"
                    "これらのタスク間の関連性が低い可能性があります。"
                )
                coherence_issues.append(issue)

        if coherence_issues:
            error_message = "計画の意味的一貫性に問題があります:\n" + "\n".join(coherence_issues)
            return False, error_message

        return True, "計画は意味的に一貫しています。"