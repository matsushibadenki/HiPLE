# path: ./agents/consultant_agent.py
# title: Consultant Agent
# description: 他のエキスパートに助言を求め、その内容を要約して返すエージェント。

from typing import List, Dict
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import SubTask, ExpertModel
from agents.base_agent import BaseAgent

class ConsultantAgent(BaseAgent):
    """
    他のエキスパートに助言を求め、その結果を統合するエージェント。
    """
    def execute(
        self,
        original_task: SubTask,
        primary_expert: ExpertModel,
        all_experts: List[ExpertModel]
    ) -> str:
        """
        指定されたタスクについて、専門家に助言を求め、結果を要約する。

        Args:
            original_task (SubTask): 元のタスク。
            primary_expert (ExpertModel): タスクの主担当エキスパート。
            all_experts (List[ExpertModel]): 利用可能なすべてのエキスパートのリスト。

        Returns:
            str: 各エキスパートからの助言をまとめたサマリー。
        """
        consulting_experts = [
            e for e in all_experts
            if e.name in original_task.consultation_experts and e.name != primary_expert.name
        ]

        if not consulting_experts:
            return "追加の助言はありません。"

        print(f"🤝 {primary_expert.name} のために、{[e.name for e in consulting_experts]} へ助言を求めます...")

        advice_list: List[str] = []
        for expert in consulting_experts:
            advice = self._get_advice_from_expert(original_task, primary_expert, expert)
            if advice:
                advice_list.append(f"### {expert.name}からの助言:\n{advice}\n")

        if not advice_list:
            return "有益な助言は得られませんでした。"

        # 助言をHRMに要約させる
        summarizer_expert = self._find_expert("HRM", all_experts)
        return self._summarize_advice(advice_list, summarizer_expert)

    def _get_advice_from_expert(self, original_task: SubTask, primary_expert: ExpertModel, consulting_expert: ExpertModel) -> str:
        """単一のエキスパートから助言を取得する。"""
        system_prompt = f"""あなたは、他のAIエキスパートのタスク遂行を支援する、優秀なコンサルタントです。
あなたの専門分野は「{consulting_expert.description}」です。
これから、エキスパート「{primary_expert.name}」が担当するタスクが提示されます。
あなたの専門的な観点から、そのタスクをより良く達成するための具体的なアイデア、注意点、代替アプローチなどを助言してください。
回答は簡潔かつ要点を得たものにしてください。"""

        user_prompt = f"""以下のタスクについて、専門的な助言をお願いします。

# 担当エキスパート
- **名前:** {primary_expert.name}
- **役割:** {primary_expert.description}

# タスク内容
- **目的(SSV):** {original_task.ssv_description}
- **詳細:** {original_task.description}
"""
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return self._query_llm(consulting_expert, messages)

    def _summarize_advice(self, advice_list: List[str], summarizer_expert: ExpertModel) -> str:
        """複数の助言を一つのサマリーにまとめる。"""
        if not advice_list:
            return ""

        all_advice = "\n---\n".join(advice_list)
        system_prompt = "あなたは、複数の専門家からの助言を整理し、要点を抽出して、実行可能な一つのサマリーにまとめる編集者です。各助言の重要な部分を抽出し、簡潔にまとめてください。"
        user_prompt = f"以下の専門家からの助言を一つのサマリーにまとめてください:\n\n{all_advice}"

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        summary = self._query_llm(summarizer_expert, messages)
        print(f"📝 助言の要約が完了しました。")
        return summary

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> ExpertModel:
        """特定のエキスパートを見つける。"""
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        raise ValueError(f"エキスパート '{name}' が見つかりません。")