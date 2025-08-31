# path: ./agents/planner_agent.py
# title: Hierarchical PlannerAgent (Self-Evaluation Aware)
# description: エキスパートが利用可能なツールを認識し、計画にツール利用ステップを組み込むことができる。

import json
import re
from typing import List, Optional, Dict, Any
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

        response_data = self._query_llm(planner_expert, messages)
        raw_response = response_data.get("response", "")
        
        return self._parse_plan_from_response(raw_response, prompt, planner_expert)

    def _find_planner_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        fallback = next((e for e in experts if e.chat_format != "diffusion"), None)
        if fallback: return fallback
        raise ValueError("利用可能なプランナーエキスパートが見つかりません。")

    def _build_system_prompt(self, expert_descriptions: str, tool_descriptions: str, performance_summary: Optional[str]) -> str:
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        prompt_header = """あなたは、ユーザーの曖昧な要求を構造化された階層的計画に変換する、超優秀なAIプロジェクトマネージャーです。
# あなたのタスク
ユーザーの要求と利用可能なリソース（エキスパート、ツール）を分析し、最適なJSON形式の実行計画を立案してください。
"""
        tools_section = f"""
# 利用可能なツール
{tool_descriptions}

# 【重要】ツールの使い方
- ツールはエキスパートではありません。`expert_name` や `consultation_experts` にツール名を入れてはいけません。
- ツールを使うには、**実行したい内容を `description` に具体的に記述し、そのタスクを遂行できるエキスパート（通常は 'Jamba'）に割り当てます。**
- 例: 「Wikipediaを使って量子コンピュータについて調査する」というタスクを 'Jamba' に割り当てる。
"""
        
        experts_section = f"""
# 利用可能なエキスパート (タスクの担当者)
{expert_descriptions}
"""

        judgement_criteria = """
# 判断基準 (最重要)
1.  **ツール利用の計画**: 最新情報や外部知識が必要な場合、まずツール利用を指示するタスクを計画に含めます。
2.  **エキスパートの選定**: `expert_name` と `consultation_experts` には、必ず上記の「利用可能なエキスパート」リストに存在する名前を指定します。
3.  **性能・速度・コスト**: `performance_summary` を参考に、タスク内容に最も適したエキスパートを選択します。
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        performance_section = f"""
# エキスパートのパフォーマンス実績 (参考情報)
{performance_summary if performance_summary else "パフォーマンス記録はまだありません。エキスパートの特性に基づいて判断してください。"}
"""
        return (prompt_header + tools_section + experts_section + judgement_criteria + 
                performance_section + self._get_json_format_section() + self._get_rules_section())

    def _build_user_prompt(self, prompt: str, validation_error: Optional[str], failed_plan: Optional[Plan]) -> str:
        user_prompt = f"以下のユーザー要求に対する階層的実行計画をJSON形式で作成してください:\n\n要求: \"{prompt}\""
        if validation_error:
            user_prompt += f"\n\n#【最重要】前回の計画は以下の検証エラーで失敗しました。このエラーを完全に修正し、論理的に一貫した新しい計画を立て直してください。\nエラー内容: {validation_error}"
        if failed_plan:
            user_prompt += f"\n\n# 警告\n前回の計画は実行に失敗しました。内容を根本的に見直し、新しいアプローチで計画を立て直してください。"
        return user_prompt

    def _parse_plan_from_response(self, raw_response: Any, original_prompt: str, planner_expert: ExpertModel) -> Plan:
        try:
            print(f"--- Hierarchical Planner Raw Response ---\n{raw_response}\n--------------------------")
            
            # BaseAgentが既にJSONをパースしてdictを返すため、型をチェックして二重パースを避ける
            plan_data: Dict[str, Any]
            if isinstance(raw_response, dict):
                plan_data = raw_response  # 既に辞書オブジェクトの場合
            elif isinstance(raw_response, str):
                plan_data = json.loads(raw_response) # 文字列の場合のみパース
            else:
                # 予期しない型の場合、エラーを発生させる
                raise TypeError(f"Response is not a valid type (string or dictionary), but got {type(raw_response)}")

            milestones = [Milestone(**m) for m in plan_data.get("milestones", [])]
            tasks_data = plan_data.get("tasks", [])
            if not tasks_data:
                 return self._create_fallback_plan(original_prompt, planner_expert)

            for t in tasks_data:
                t.setdefault("ssv_description", t["description"])
                t.setdefault("consultation_experts", [])
                t.setdefault("reviewer_expert", None)
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
        task = SubTask(
            task_id=1,
            milestone_id=1,
            description=original_prompt,
            expert_name=expert.name,
            ssv_description=original_prompt,
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
        return "\n".join(
            [f"- **{e.name}**: {e.description} (Cost: {e.cost_score}/10, Speed: {e.speed_score}/10)" 
             for e in experts if e.name.lower() != "reporter"]
        )

    def _get_json_format_section(self) -> str:
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        return """
# JSON出力フォーマット (厳守)
あなたの応答は、最終的に自己評価を含むより大きなJSONの一部として解析されます。以下の`response`キーの値として、計画JSONを出力してください。
`response`キーの値は、純粋な計画JSONオブジェクトである必要があります。
```json
{
    "response": {
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
                "description": "ツール `wikipedia_search` を使って「HRMモデル」の概要を調査する",
                "expert_name": "Jamba",
                "ssv_description": "HRMモデルの概要調査",
                "consultation_experts": [],
                "reviewer_expert": "HRM",
                "dependencies": []
            },
            {
                "task_id": 2,
                "milestone_id": 1,
                "description": "タスク1の結果を基に、HRMモデルの特徴をまとめる",
                "expert_name": "HRM",
                "ssv_description": "HRMモデルの特徴を要約",
                "consultation_experts": [],
                "reviewer_expert": null,
                "dependencies": [1]
            }
        ]
    },
    "self_evaluation": { ... }
}
```
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def _get_rules_section(self) -> str:
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        return """
# ルール
- **ID**: `milestone_id`と`task_id`は1から始まる連番にしてください。
- **依存関係**: `dependencies`には、先行するタスクの`task_id`を**数値の配列**として`[1, 2]`のように指定します。
- **担当者**: `expert_name` と `consultation_experts` には、必ずエキスパートリストの名前を指定してください。ツール名は指定できません。
- **報告タスク**: 複雑な要求の場合、最後に'Reporter'を配置し、最終報告書を作成させてください。
- **単純な要求**: 単純な挨拶や質問の場合、マイルストーンは1つ、タスクも1つだけ生成します。
"""
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

