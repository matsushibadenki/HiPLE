# path: ./agents/emergence_agent.py
# title: Emergence Agent for Creative Brainstorming
# description: Orchestrates a multi-expert brainstorming session to generate novel ideas.

from typing import List, Dict, Any, Optional
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent
from services.model_loader import ModelLoaderService
from llama_cpp.llama_types import ChatCompletionRequestMessage

class EmergenceAgent(BaseAgent):
    """
    複数の専門家エージェントによる議論を促進し、
    単一のエージェントでは到達できない創発的なアイデアや解決策を生み出すエージェント。
    """
    def __init__(self, model_loader: ModelLoaderService):
        super().__init__(model_loader)
        self.discussion_rounds = 2 # 議論のターン数

    def execute(self, prompt: str, all_experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        指定されたプロンプトについて、ブレインストーミングセッションを実行する。
        """
        print(f"✨ 創発セッションを開始します: {prompt}")

        # 1. 議論に参加する多様なエキスパートを選出
        participants = self._select_participants(all_experts)
        if len(participants) < 2:
            return {
                "response": "創発セッションに必要なエキスパートが不足しています。",
                "self_evaluation": {"confidence": 0.1, "reasoning": "Could not find enough diverse experts to hold a discussion."}
            }
        
        print(f"👥 参加者: {[p.name for p in participants]}")

        # 2. マルチターンでの議論を実行
        discussion_history = f"# 議題: {prompt}\n\n"
        for i in range(self.discussion_rounds):
            print(f"🔄 議論ラウンド {i+1}/{self.discussion_rounds}")
            for expert in participants:
                print(f"   🗣️ {expert.name} のターン...")
                contribution_prompt = self._create_contribution_prompt(prompt, discussion_history, expert)
                messages: List[ChatCompletionRequestMessage] = [
                    {"role": "system", "content": expert.system_prompt},
                    {"role": "user", "content": contribution_prompt}
                ]
                
                response_data = self._query_llm(expert, messages)
                contribution = response_data.get("response", f"（{expert.name}は応答しませんでした）")

                discussion_history += f"## {expert.name} (専門: {expert.description}) の意見:\n{contribution}\n\n---\n"

        # 3. 最終的な統合役が議論を要約し、創発的な結論を導き出す
        synthesizer = self._find_expert("HRM", all_experts)
        if not synthesizer:
             synthesizer = participants[0] # フォールバック
        
        print(f"✅ 議論が終了しました。統合役 ({synthesizer.name}) が結論をまとめます。")
        synthesis_prompt = self._create_synthesis_prompt(prompt, discussion_history)
        messages_synth: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": "あなたは、複数の専門家による活発な議論を分析し、そこから最も重要で革新的な洞察を抽出し、一つの首尾一貫した結論に統合する、極めて優秀なファシリテーター兼エディターです。"},
            {"role": "user", "content": synthesis_prompt}
        ]
        
        final_result_data = self._query_llm(synthesizer, messages_synth)
        print("✨ 創発セッションが完了しました。")
        
        return final_result_data

    def _select_participants(self, all_experts: List[ExpertModel]) -> List[ExpertModel]:
        """議論のために多様なエキスパートを選択する"""
        selected_experts = []
        # 思考(HRM)、汎用(Jamba)、コーディング(Transformer)を優先的に選出
        participant_names = ["hrm", "jamba", "transformer"]
        for name in participant_names:
            expert = self._find_expert(name, all_experts)
            if expert:
                selected_experts.append(expert)
        return selected_experts

    def _create_contribution_prompt(self, original_prompt: str, history: str, current_expert: ExpertModel) -> str:
        """各エキスパートに意見を求めるためのプロンプトを生成する"""
        return f"""現在、以下の議題についてブレインストーミングを行っています。
これまでの議論を踏まえ、あなたの専門分野である「{current_expert.description}」の観点から、ユニークで建設的な意見、アイデア、または批判的視点を提供してください。

{history}

あなたの意見を簡潔に述べてください。
"""

    def _create_synthesis_prompt(self, original_prompt: str, history: str) -> str:
        """最終的な結論を統合するためのプロンプトを生成する"""
        return f"""以下の議題に関する専門家たちのブレインストーミングの全記録です。

{history}

# あなたへの最終指示
この議論全体を注意深く分析し、以下の点を満たす最終的な結論を一つにまとめてください:
1.  **統合:** 個々の意見をただ並べるのではなく、それらを統合して新しい一つの洞察（創発的アイデア）を形成してください。
2.  **革新性:** 最も革新的で、元の議題に対するユニークな解決策や視点を強調してください。
3.  **明確性:** 誰が読んでも理解できるように、明確かつ簡潔な言葉で記述してください。

最終的な結論のみを出力してください。
"""

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> Optional[ExpertModel]:
        """特定のエキスパートを見つける。"""
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        return None
