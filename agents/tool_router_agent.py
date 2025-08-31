# path: ./agents/tool_router_agent.py
# title: Intelligent Tool Router Agent (Self-Aware)
# description: Uses LLM reasoning to understand user intent, including meta-questions about the AI system itself.

import json
import re
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from domain.schemas import ExpertModel
from agents.base_agent import BaseAgent

class ToolRouterAgent(BaseAgent):
    """
    ユーザーの要求の意図を分析し、適切なツールや処理フローを特定するインテリジェントなルーター。
    """
    def execute(self, prompt: str, experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        プロンプトを分析し、ツール、クエリ、URLを含む辞書を返す。
        """
        # ルーティングには思考能力の高いHRMモデルを指名
        router_expert = self._find_expert("HRM", experts)
        if not router_expert:
            # フォールバックとして利用可能な最初のエキスパートを使用
            router_expert = next((e for e in experts if e.chat_format != "diffusion"), None)
        
        if not router_expert:
            raise ValueError("No suitable expert found for routing.")

        print(f"🧠 Router expert selected: {router_expert.name}")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        system_prompt = (
            "あなたはユーザーの要求の意図を深く分析し、その要求を達成するために最も適した処理を判断する、超優秀なディスパッチャーです。\n"
            "以下の思考プロセスに従い、最終的な判断をJSONフォーマットで出力してください。\n\n"
            "# 思考プロセス (Step-by-Step)\n"
            "1.  **要求の核心分析**: ユーザーは何を本当に知りたいのか、または何をしてほしいのか？（例：「作り方を知りたい」「歴史を知りたい」など）\n"
            "2.  **情報源の特定**: その要求に答えるために必要な情報は、外部の普遍的な知識か、最新情報か、あるいはAI自身の内部情報か？\n"
            "3.  **処理の分類**: 上記の分析に基づき、以下の基準で最適な処理を一つだけ選択する。\n"
            "4.  **JSON生成**: 最終的な判断をJSON形式で出力する。思考プロセスは出力に含めないこと。\n\n"
            "# 判断基準\n"
            "- `wikipedia`: **「普遍的で確立された外部の知識」**が求められている場合。一般的な用語、歴史、人物、科学的原理など。\n"
            "    - 例: 「徳川家康とは？」「量子もつれの原理」\n"
            "- `web_search`: **「最新情報」「特定のURLに関する情報」「具体的な手順やレシピ」**が求められている場合。\n"
            "    - 例: 「今日のニュースを教えて」「この記事(URL)を要約して」「アイスクリームの作り方を教えて」\n"
            "- `emergent_task`: **「新しいアイデアや創造的な解決策」**が求められている場合。ブレインストーミングの指示。\n"
            "    - 例: 「新商品のアイデアをブレストして」\n"
            "- `complex_task`: **「AI自身に関する質問」**または**「複数ステップの実行や専門的なコード生成」**が求められている場合。\n"
            "    - 例: 「HRMモデルについて教えて」「君の能力は？」「PythonでWebサーバーを作って」\n"
            "- `greeting`: **「単純な対話」**の場合。挨拶や感謝など。\n"
            "    - 例: 「こんにちは」「ありがとう」\n\n"
            "# 出力フォーマット (厳守)\n"
            "```json\n"
            "{\n"
            '  "tool": "（\'wikipedia\', \'web_search\', \'emergent_task\', \'complex_task\', \'greeting\' のいずれか）",\n'
            '  "query": "（ツールやタスクで使用すべきキーワードや質問文。挨拶の場合はnull）",\n'
            '  "url": "（web_searchの場合のURL。それ以外はnull）"\n'
            "}\n"
            "```"
        )
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        # ToolRouterAgent自身の実行では自己評価は不要なため、内部のLLM呼び出しを直接行う
        raw_response_data = self._query_llm(router_expert, messages)
        raw_response = raw_response_data.get("response", "")
        
        try:
            json_match = re.search(r'```json\s*(\{[\s\S]*?\})\s*```', raw_response, re.DOTALL)
            if json_match:
                response_json_str = json_match.group(1)
            else:
                response_json_str = raw_response[raw_response.find('{'):raw_response.rfind('}')+1]

            data = json.loads(response_json_str)
            tool = data.get("tool", "complex_task")
            query = data.get("query")
            url = data.get("url")
            response = data.get("response") # 挨拶用

            if tool not in ["wikipedia", "web_search", "complex_task", "greeting", "emergent_task"]:
                tool = "complex_task"

            return {"type": tool, "query": query if query else prompt, "url": url, "response": response}

        except (json.JSONDecodeError, AttributeError):
            # パース失敗時は最も安全なcomplex_taskとして処理
            return {"type": "complex_task", "query": prompt, "url": None, "response": None}

    def _find_expert(self, name: str, experts: List[ExpertModel]) -> Optional[ExpertModel]:
        for expert in experts:
            if expert.name.lower() == name.lower():
                return expert
        return None