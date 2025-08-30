# path: ./agents/reviewer_agent.py
# title: Reviewer Agent (Self-Evaluation Aware)
# description: 他のエキスパートが生成した成果物をレビューし、自己評価付きのフィードバックを提供するエージェント。

from typing import List, Dict, Any
from llama_cpp.llama_types import ChatCompletionRequestMessage
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel, SubTask

class ReviewerAgent(BaseAgent):
    """
    成果物をレビューし、フィードバックを提供するエージェント。
    """
    def execute(
        self,
        task: SubTask,
        generated_output: str,
        reviewer_expert: ExpertModel,
        original_expert: ExpertModel
    ) -> Dict[str, Any]:
        """
        生成された成果物をレビューし、改善点を指摘する。
        """
        print(f"🧐 {reviewer_expert.name}が{original_expert.name}の成果物をレビューします...")

        system_prompt = f"""あなたは、他のAIエキスパートが生成した成果物をレビューし、品質を向上させるための具体的で建設的なフィードバックを与える、非常に優秀な品質保証（QA）スペシャリストです。
あなたの専門分野は「{reviewer_expert.description}」です。"""

        user_prompt = f"""以下のタスクと、それに対してエキスパート「{original_expert.name}」が生成した成果物をレビューしてください。

# 元のタスク
- **目的 (SSV):** {task.ssv_description}
- **詳細:** {task.description}

# 生成された成果物
---
{generated_output}
---

# あなたへの指示
上記の成果物が、元のタスクの目的（SSV）と詳細を完全に満たしているか、あなたの専門的観点から厳しく評価してください。
問題点や改善できる点があれば、具体的で実行可能な修正案を箇条書きで指摘してください。
もし成果物が完璧で修正の必要がない場合は、「修正の必要はありません。」という一文のみを返してください。
"""
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        feedback_data = self._query_llm(reviewer_expert, messages)
        print(f"📝 レビューが完了しました。")
        return feedback_data
