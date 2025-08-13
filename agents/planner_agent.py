# path: ./agents/planner_agent.py
# title: Hierarchical PlannerAgent with Performance-Awareness
# description: エキスパートのパフォーマンス情報を考慮して、他のエキスパートへの相談を含む階層的な計画を生成する。

import json
import re
from typing import List, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import Plan, SubTask, ExpertModel, Milestone
from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    """
    ユーザーの要求を分析し、階層的な計画（Plan）を生成するエージェント (HiPLE-P)
    エキスパートのパフォーマンスも考慮する
    """
    def execute(
        self,
        prompt: str,
        experts: List[ExpertModel],
        failed_plan: Optional[Plan] = None,
        validation_error: Optional[str] = None,
        performance_summary: Optional[str] = None # 追加
    ) -> Plan:
        planner_expert = self._find_planner_expert(experts)
        expert_descriptions = self._format_expert_descriptions(experts)

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        system_prompt = self._build_system_prompt(expert_descriptions, performance_summary)
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
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

    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    def _build_system_prompt(self, expert_descriptions: str, performance_summary: Optional[str]) -> str:
        prompt_header = """あなたは、ユーザーの曖昧な要求を構造化された階層的計画に変換する、超優秀なAIプロジェクトマネージャーです。

# あなたのタスク
ユーザーの要求とエキスパートのパフォーマンス実績を分析し、以下のルールに従ってJSON形式の実行計画を立案してください。

1.  **階層化**: 思考を3つのレベル（L1: 全体目標, L2: マイルストーン, L3: サブタスク）に分解します。
2.  **エキスパート選定 (最重要)**: 各タスクに最適なエキスパートを `expert_name` に割り当ててください。**エキスパートのパフォーマンスサマリーを最優先の判断材料とし、スコアが高く、タスク内容に適したエキスパートを選択**してください。
3.  **意味構造の定義**: 各サブタスク（L3）には、そのタスクの本質的な意味を凝縮した短い説明文 `ssv_description` を必ず設定してください。
4.  **コンサルテーション**: タスクの品質向上のため、複数の専門知識が必要だと判断した場合、`consultation_experts`フィールドに助言を求めるべきエキスパート名のリストを指定してください。
"""

        experts_section = f"""
# 利用可能なエキスパート
{expert_descriptions}
"""
        
        performance_section = f"""
# エキスパートのパフォーマンス実績 (最重要参考情報)
{performance_summary if performance_summary else "パフォーマンス記録はまだありません。エキスパートの説明に基づいて判断してください。"}
"""

        json_format_section = """
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
      "expert_name": "（パフォーマンスと適性を考慮して選んだエキスパート名）",
      "ssv_description": "（タスクの意味の核を記述した短い説明文）",
      "consultation_experts": ["（助言を求めるエキスパート名1）"],
      "dependencies": []
    }
  ]
}
```
"""

        rules_section = """
# ルール
- **ID**: `milestone_id`と`task_id`は1から始まる連番にしてください。
- **依存関係**: `dependencies`には先行タスクの`task_id`をリストで指定します。
- **報告タスク**: 複雑な要求の場合、最後に'Reporter'を配置し、最終報告書を作成させてください。
- **単純な要求**: 単純な挨拶や質問の場合、マイルストーンは1つ、タスクも1つだけ生成します。
"""
        return prompt_header + experts_section + performance_section + json_format_section + rules_section
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    def _build_user_prompt(self, prompt: str, validation_error: Optional[str], failed_plan: Optional[Plan]) -> str:
        user_prompt = f"以下のユーザー要求に対する階層的実行計画をJSON形式で作成してください:\n\n要求: \"{prompt}\""
        if validation_error:
            user_prompt += f"\n\n#【最重要】前回の計画は以下の検証エラーで失敗しました。このエラーを完全に修正し、論理的に一貫した新しい計画を立て直してください。\nエラー内容: {validation_error}"
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
            tasks_data = plan_data.get("tasks", [])
            if not tasks_data:
                 # フォールバック：単純なタスクとして生成
                 return self._create_fallback_plan(original_prompt, planner_expert)

            for t in tasks_data:
                if "ssv_description" not in t or not t["ssv_description"]:
                    t["ssv_description"] = t["description"]
                if "consultation_experts" not in t:
                    t["consultation_experts"] = []

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
        """パース失敗時に、単純な直接実行計画を作成する"""
        task = SubTask(
            task_id=1,
            milestone_id=1,
            description=original_prompt,
            expert_name=expert.name,
            ssv_description=original_prompt,
            consultation_experts=[],
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
