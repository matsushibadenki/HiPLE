# path: ./agents/planner_agent.py
# title: Hierarchical PlannerAgent (HiPLE-P)
# description: ユーザーの要求を分析し、階層的な実行計画（L1, L2, L3）を生成する。

import json
import re
from typing import List, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import Plan, SubTask, ExpertModel, Milestone
from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    """
    ユーザーの要求を分析し、階層的な計画（Plan）を生成するエージェント (HiPLE-P)
    """
    def execute(
        self,
        prompt: str,
        experts: List[ExpertModel],
        failed_plan: Optional[Plan] = None,
        validation_error: Optional[str] = None
    ) -> Plan:
        planner_expert = self._find_planner_expert(experts)
        expert_descriptions = self._format_expert_descriptions(experts)

        system_prompt = self._build_system_prompt(expert_descriptions)
        user_prompt = self._build_user_prompt(prompt, validation_error, failed_plan)
        
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        raw_response = self._query_llm(planner_expert, messages)
        
        return self._parse_plan_from_response(raw_response, prompt, planner_expert)

    def _find_planner_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        # 思考の中心はHRMが担う
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        # フォールバック
        for expert in experts:
            if expert.chat_format != "diffusion": return expert
        raise ValueError("利用可能なプランナーエキスパートが見つかりません。")

    def _build_system_prompt(self, expert_descriptions: str) -> str:
        return f"""あなたは、ユーザーの曖昧な要求を構造化された階層的計画に変換する、超優秀なAIプロジェクトマネージャーです。

# あなたのタスク
ユーザーの要求を分析し、以下の3つのレベルで構成されるJSON形式の実行計画を立案してください。

1.  **L1: 全体目標 (overall_goal)**: ユーザー要求の最終的なゴールを、一文で明確に定義します。
2.  **L2: 主要マイルストーン (milestones)**: 全体目標を達成するための、論理的な中間ステップを複数定義します。各マイルストーンは「章」のようなものです。
3.  **L3: 具体的なサブタスク (tasks)**: 各マイルストーンを達成するための、実行可能な具体的なタスクを定義します。各タスクには、最適なエキスパートを1名割り当てます。

# 厳守すべきルール
- **階層構造**: 必ず `overall_goal`, `milestones`, `tasks` の3階層で計画を作成してください。
- **IDの連番**: `milestone_id` と `task_id` は必ず1から始まる連番にしてください。
- **タスクとマイルストーンの紐付け**: 各タスクには、それが属する `milestone_id` を必ず設定してください。
- **依存関係**: タスクの `dependencies` には、そのタスクが依存する先行タスクの `task_id` をリストで指定します。
- **報告タスク**: 複雑な要求の場合、最後のマイルストーンの最後のタスクとして、必ず 'Reporter' を配置し、それまでの全タスクを統合して最終報告書を作成させてください。
- **単純な要求**: 「こんにちは」のような単純な挨拶や質問の場合、マイルストーンは1つ、タスクも1つだけ生成します。Reporterは不要です。
- **エキスパートの能力**: エキスパートは以下の能力しか持ちません。Web検索やリアルタイム情報の取得はできません。
{expert_descriptions}

# 出力フォーマット (JSON形式のみ)
```json
{{
  "overall_goal": "（L1: ユーザー要求を一文で表現した最終目標）",
  "milestones": [
    {{
      "milestone_id": 1,
      "title": "（L2: 最初のマイルストーンのタイトル）",
      "description": "（このマイルストーンの目的）"
    }}
  ],
  "tasks": [
    {{
      "task_id": 1,
      "milestone_id": 1,
      "description": "（L3: 実行すべき具体的なタスク内容）",
      "expert_name": "（エキスパート名）",
      "dependencies": []
    }}
  ]
}}
```"""

    def _build_user_prompt(self, prompt: str, validation_error: Optional[str], failed_plan: Optional[Plan]) -> str:
        user_prompt = f"以下のユーザー要求に対する階層的実行計画をJSON形式で作成してください:\n\n要求: \"{prompt}\""
        if validation_error:
            user_prompt += f"\n\n# 警告\n前回の計画は検証エラーで失敗しました: {validation_error}\nこのエラーを修正し、正しい計画を立て直してください。"
        if failed_plan:
            user_prompt += f"\n\n# 警告\n前回の計画は実行に失敗しました。内容を根本的に見直し、新しいアプローチで計画を立て直してください。"
        return user_prompt

    def _parse_plan_from_response(self, raw_response: str, original_prompt: str, planner_expert: ExpertModel) -> Plan:
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
            tasks = [SubTask(**t) for t in plan_data.get("tasks", [])]

            return Plan(
                original_prompt=original_prompt,
                overall_goal=plan_data.get("overall_goal", "N/A"),
                milestones=milestones,
                tasks=tasks
            )
        except (json.JSONDecodeError, TypeError, ValueError, AttributeError) as e:
            print(f"❌ 階層的計画のパースに失敗しました: {e}")
            print(f"🔁 フォールバック：元のプロンプトを直接実行します。")
            task = SubTask(
                task_id=1,
                milestone_id=1,
                description=original_prompt,
                expert_name=planner_expert.name,
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
        return "\n".join([f"- **{e.name}**: {e.description}" for e in experts if e.name.lower() != "reporter"])