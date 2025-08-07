# path: ./agents/reporter_agent.py
# title: Finalized Reporter Agent
# description: 全タスクの成果を統合し、ユーザーの元の要求に、元の言語で的確に回答する最終版。

from typing import List
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import Plan, ExpertModel
from agents.base_agent import BaseAgent

class ReporterAgent(BaseAgent):
    """
    完了した階層的計画の結果を統合し、最終的な報告書を生成するエージェント
    """
    def execute(self, plan: Plan, experts: List[ExpertModel]) -> str:
        reporter_expert = self._find_reporter_expert(experts)
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        context = self._build_context(plan)
        prompt = self._build_final_prompt(plan.original_prompt, context)
        
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": reporter_expert.system_prompt},
            {"role": "user", "content": prompt}
        ]
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        return self._query_llm(reporter_expert, messages)

    def _find_reporter_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        """レポーター役のエキスパートを見つける"""
        for expert in experts:
            if expert.name.lower() == "reporter":
                return expert
        # HRMは安定したフォールバック先
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        raise ValueError("レポーター役のエキスパートが見つかりません。")

    def _build_context(self, plan: Plan) -> str:
        """レポーターに渡すための、全タスクの結果をまとめたコンテキストを構築する"""
        context = f"# 最終目標: {plan.overall_goal}\n\n# 各エキスパートからの報告サマリー\n---\n"
        # 実行順にタスクをソート
        sorted_tasks = sorted([t for t in plan.tasks if t.status == "completed" and t.expert_name.lower() != 'reporter'], key=lambda t: t.task_id)
        
        for task in sorted_tasks:
            context += f"## タスク {task.task_id}: {task.description} (担当: {task.expert_name})\n"
            context += f"**結果:**\n{task.result}\n\n"
        context += "---\n"
        return context

    def _build_final_prompt(self, original_prompt: str, context: str) -> str:
        """最終的な指示を生成するための、明確で強力なプロンプトを構築する"""
        return f"""\
あなたは、複数のAIエキスパートからの報告を統合し、最終的な一つの回答を作成する、極めて優秀なチーフエディターです。

{context}

# あなたへの最終指示 (最重要)
上記の「各エキスパートからの報告サマリー」を完全に理解し、以下のユーザーからの「元の要求」に、直接的かつ包括的に回答してください。

## 元の要求
「{original_prompt}」

# 厳守すべきルール
1.  **言語の厳守:** 回答は、必ず「元の要求」と同じ言語（この場合は日本語）で記述してください。
2.  **内容の統合:** 単なる報告の連結ではなく、全ての情報を統合・要約し、首尾一貫した一つの文章に再構成してください。
3.  **目的の遵守:** あなたの唯一の目的は、「元の要求」に答えることです。報告サマリーにない情報は、決して含めないでください。
4.  **形式:** 最終的な回答のみを出力してください。思考過程や挨拶などは一切不要です。
"""