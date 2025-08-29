# path: ./agents/critic_agent.py
# title: Critic Agent for Plan Evaluation
# description: A specialized agent that reviews a generated plan for strategic flaws and inefficiencies.

from typing import List
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import Plan, ExpertModel
from agents.base_agent import BaseAgent

class CriticAgent(BaseAgent):
    """
    生成された計画全体をレビューし、戦略的な欠陥や非効率性を指摘する批評家エージェント。
    """
    def execute(self, plan: Plan, experts: List[ExpertModel]) -> str:
        """
        計画をレビューし、改善のためのフィードバック、または承認のメッセージを返す。
        """
        critic_expert = self._find_critic_expert(experts)
        plan_str = self._format_plan_for_review(plan)

        system_prompt = """あなたは、AIプロジェクトマネージャーが作成した実行計画をレビューする、超優秀な戦略コンサルタントです。
あなたの役割は、計画の構造的な正しさだけでなく、その「戦略的な妥当性」を厳しく評価することです。

# 評価の観点
- **過不足**: 目標達成に不要なタスクはないか？逆に、欠けている重要なステップはないか？
- **効率性**: タスクの順序は最適か？もっと効率的な進め方はないか？
- **エキスパート選定**: 各タスクに割り当てられたエキスパートは本当に最適か？より適任なエキスパートはいないか？
- **リスク**: 計画に潜むリスクや、失敗する可能性の高い箇所はないか？

# あなたへの指示
提示された計画を上記の観点から評価し、具体的で建設的な改善案を箇条書きで指摘してください。
もし計画が論理的かつ戦略的に完璧で、修正の必要がないと判断した場合は、「計画に問題は見つかりませんでした。」という一文のみを返してください。
"""

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": plan_str}
        ]
        
        feedback = self._query_llm(critic_expert, messages)
        print(f"🧐 批評家エージェントによる計画レビューが完了しました。")
        return feedback

    def _find_critic_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        # 批評にも論理的推論が得意なHRMモデルを利用
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        # フォールバック
        for expert in experts:
            if expert.chat_format != "diffusion": return expert
        raise ValueError("利用可能な批評家エキスパートが見つかりません。")

    def _format_plan_for_review(self, plan: Plan) -> str:
        """
        PlanオブジェクトをLLMがレビューしやすい文字列形式に変換する。
        """
        lines = [f"# レビュー対象の計画: {plan.overall_goal}\n"]

        for milestone in sorted(plan.milestones, key=lambda m: m.milestone_id):
            lines.append(f"\n## マイルストーン {milestone.milestone_id}: {milestone.title}")
            lines.append(f"   - 説明: {milestone.description}")
            
            tasks_in_milestone = sorted(
                [t for t in plan.tasks if t.milestone_id == milestone.milestone_id],
                key=lambda t: t.task_id
            )
            
            for task in tasks_in_milestone:
                lines.append(f"###    - タスク {task.task_id}: {task.description}")
                lines.append(f"       - 担当: {task.expert_name}")
                if task.dependencies:
                    lines.append(f"       - 依存関係: {task.dependencies}")
                if task.reviewer_expert:
                    lines.append(f"       - レビュアー: {task.reviewer_expert}")
        
        return "\n".join(lines)
