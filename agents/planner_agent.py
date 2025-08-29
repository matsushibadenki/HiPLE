# path: ./agents/planner_agent.py
# title: Hierarchical PlannerAgent (Tool-Aware)
# description: エキスパートが利用可能なツールを認識し、計画にツール利用ステップを組み込むことができる。

import json
import re
from typing import List, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import Plan, SubTask, ExpertModel, Milestone
from agents.base_agent import BaseAgent
from services.tool_manager_service import ToolManagerService

class PlannerAgent(BaseAgent):
    """
    ユーザーの要求を分析し、階層的な計画（Plan）を生成するエージェント (HiPLE-P)
    エキスパートのパフォーマンス、コスト、速度、利用可能なツールも考慮する。
    """
    def execute(
        self,
        prompt: str,
        experts: List[ExpertModel],
        tool_manager: ToolManagerService,
        failed_plan: Optional[Plan] = None,
        validation_error: Optional[str] = None,
        performance_summary: Optional[str] = None,
    ) -> Plan:
        planner_expert = self._find_planner_expert(experts)
        expert_descriptions = self._format_expert_descriptions(experts)
        tool_descriptions = tool_manager.get_tool_descriptions()

        system_prompt = self._build_system_prompt(expert_descriptions, tool_descriptions, performance_summary)
        user_prompt = self._build_user_prompt(prompt, validation_error, failed_plan)
        
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        raw_response = self._query_llm(planner_expert, messages)
        
        return self._parse_plan_from_response(raw_response, prompt, planner_expert)

    def _find_planner_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        for expert in experts:
            if expert.chat_format != "diffusion": return expert
        raise ValueError("利用可能なプランナーエキスパートが見つかりません。")

    def _build_system_prompt(self, expert_descriptions: str, tool_descriptions: str, performance_summary: Optional[str]) -> str:
        prompt_header = """あなたは、ユーザーの曖昧な要求を構造化された階層的計画に変換する、超優秀なAIプロジェクトマネージャーです。
# あなたのタスク
ユーザーの要求と利用可能なリソース（エキスパート、ツール）を分析し、最適なJSON形式の実行計画を立案してください。
"""
        tools_section = f"""
# 利用可能なツール
{tool_descriptions}
- タスク記述に「ツールを使って〜を調べる」のように具体的に指示することで、エキスパートはツールを利用できます。
"""
        
        experts_section = f"""
# 利用可能なエキスパート
{expert_descriptions}
"""

        judgement_criteria = """
# 判断基準 (最重要)
1.  **ツール利用**: 最新情報や専門知識が必要な場合、まずツール利用のタスクを計画してください。
2.  **性能 (Performance)**: `performance_summary` の `Score` が高いエキスパートを優先します。
3.  **速度 (Speed)** & **コスト (Cost)**: `speed_score` と `cost_score` のバランスを考慮します。
4.  **適性 (Description)**: タスク内容に最も適した能力を持つエキスパートを選択します。
"""
        
        performance_section = f"""
# エキスパートのパフォーマンス実績 (参考情報)
{performance_summary if performance_summary else "パフォーマンス記録はまだありません。エキスパートの特性に基づいて判断してください。"}
"""
        json_format_section = "..." # (変更なしのため省略)
        rules_section = "..." # (変更なしのため省略)

        return (prompt_header + tools_section + experts_section + judgement_criteria + 
                performance_section + self._get_json_format_section() + self._get_rules_section())

    def _build_user_prompt(self, prompt: str, validation_error: Optional[str], failed_plan: Optional[Plan]) -> str:
        # ... (変更なし)
        user_prompt = f"以下のユーザー要求に対する階層的実行計画をJSON形式で作成してください:\n\n要求: \"{prompt}\""
        if validation_error:
            user_prompt += f"\n\n#【最重要】前回の計画は以下の検証エラーで失敗しました。このエラーを完全に修正し、論理的に一貫した新しい計画を立て直してください。\nエラー内容: {validation_error}"
        if failed_plan:
            user_prompt += f"\n\n# 警告\n前回の計画は実行に失敗しました。内容を根本的に見直し、新しいアプローチで計画を立て直してください。"
        return user_prompt

    def _parse_plan_from_response(self, raw_response: str, original_prompt: str, planner_expert: ExpertModel) -> Plan:
        # ... (変更なし)
        try:
            print(f"--- Hierarchical Planner Raw Response ---\n{raw_response}\n--------------------------")
            json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_response, re.DOTALL)
            if not json_match:
                start_index = raw_response.find('{')
                end_index = raw_response.rfind('}')
                if start_index == -1 or end_index == -1:
                    raise json.JSONDecodeError("応答にJSONオブジェクトが見つかりません。", raw_response, 0)
                plan_json_str = raw_response[start_index:end_index + 1]
            else:
                plan_json_str = json_match.group(1)
            
            plan_data = json.loads(plan_json_str)

            milestones = [Milestone(**m) for m in plan_data.get("milestones", [])]
            tasks_data = plan_data.get("tasks", [])
            if not tasks_data:
                 return self._create_fallback_plan(original_prompt, planner_expert)

            for t in tasks_data:
                if "ssv_description" not in t or not t["ssv_description"]:
                    t["ssv_description"] = t["description"]
                if "consultation_experts" not in t:
                    t["consultation_experts"] = []
                if "reviewer_expert" not in t:
                    t["reviewer_expert"] = None
                t["feedback_history"] = []


            tasks = [SubTask(**t) for t in tasks_data]

            return Plan(
                original_prompt=original_prompt,
                overall_goal=plan_data.get("overall_goal", "N/A"),
                milestones=milestones,
                tasks=tasks
            )
        except (json.JSONDecodeError, TypeError, ValueError, AttributeError) as e:
            print(f"❌ 階層的計画のパースに失敗しました: {e}")
            print(f"🔁 フォールバック：元のプロンプトを直接実行します。")
            return self._create_fallback_plan(original_prompt, planner_expert)

    def _create_fallback_plan(self, original_prompt: str, expert: ExpertModel) -> Plan:
        # ... (変更なし)
        task = SubTask(
            task_id=1,
            milestone_id=1,
            description=original_prompt,
            expert_name=expert.name,
            ssv_description=original_prompt,
            consultation_experts=[],
            reviewer_expert=None,
            dependencies=[]
        )
        milestone = Milestone(milestone_id=1, title="Direct Execution", description="Execute the user's prompt directly.")
        return Plan(
            original_prompt=original_prompt,
            overall_goal=original_prompt,
            milestones=[milestone],
            tasks=[task]
        )

    def _format_expert_descriptions(self, experts: List[ExpertModel]) -> str:
        # ... (変更なし)
        return "\n".join(
            [f"- **{e.name}**: {e.description} (Cost: {e.cost_score}/10, Speed: {e.speed_score}/10)" 
             for e in experts if e.name.lower() != "reporter"]
        )

    def _get_json_format_section(self) -> str:
        return """
# JSON出力フォーマット (厳守)
```json
{
  "overall_goal": "（L1: ユーザー要求を一文で表現した最終目標）",
  "milestones": [
    {
      "milestone_id": 1,
      "title": "（L2: 最初のマイルストーンのタイトル）",
      "description": "（このマイルストーンの目的）"
    }
  ],
  "tasks": [
    {
      "task_id": 1,
      "milestone_id": 1,
      "description": "（L3: 実行すべき具体的なタスク内容）",
      "expert_name": "（性能・コスト・速度・適性を総合的に判断して選んだエキスパート名）",
      "ssv_description": "（タスクの意味の核を記述した短い説明文）",
      "consultation_experts": ["（助言を求めるエキスパート名1）"],
      "reviewer_expert": "（成果物の品質を保証するためのレビュー担当者名）",
      "dependencies": []
    }
  ]
}
```
"""

    def _get_rules_section(self) -> str:
        return """
# ルール
- **ID**: `milestone_id`と`task_id`は1から始まる連番にしてください。
- **依存関係**: `dependencies`には先行タスクの`task_id`をリストで指定します。
- **報告タスク**: 複雑な要求の場合、最後に'Reporter'を配置し、最終報告書を作成させてください。
- **単純な要求**: 単純な挨拶や質問の場合、マイルストーンは1つ、タスクも1つだけ生成します。
"""

