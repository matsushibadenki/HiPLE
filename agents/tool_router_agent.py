# path: ./agents/tool_router_agent.py
# title: Tool Router Agent with Improved Prompting
# description: Enhances routing accuracy with a more detailed and example-rich system prompt.

from typing import Dict, List, Any
from llama_cpp.llama_types import ChatCompletionRequestMessage
from agents.base_agent import BaseAgent
from domain.schemas import ExpertModel
import json
import re

class ToolRouterAgent(BaseAgent):
    """
    ユーザーのクエリを分析し、タスクの種類を分類して適切な処理フローに振り分けるエージェント (HiPLE-R)
    """

    def execute(self, prompt: str, experts: List[ExpertModel]) -> Dict[str, Any]:
        """
        クエリを分析し、タスクタイプ、クエリ、そして場合によっては直接の応答を返す。
        """
        router_expert = self._find_router_expert(experts)
        system_prompt = self._build_system_prompt()
        
        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]

        response_data = self._query_llm(router_expert, messages)
        raw_response = response_data.get("response", "")
        
        return self._parse_routing_decision(raw_response, prompt)

    def _find_router_expert(self, experts: List[ExpertModel]) -> ExpertModel:
        """
        ルーティングに適したエキスパート（HRM）を見つける。
        """
        for expert in experts:
            if expert.name.lower() == "hrm":
                return expert
        # フォールバックとして、拡散モデル以外の最初のエキスパートを使用
        fallback = next((e for e in experts if e.chat_format != "diffusion"), None)
        if fallback:
            return fallback
        raise ValueError("利用可能なルーターエキスパートが見つかりません。")

    def _build_system_prompt(self) -> str:
        return r"""
# Role: Advanced Task Router AI
Your function is to analyze the user's query and classify it into ONE of the predefined task types. You must output your decision in a specific JSON format and nothing else.

# Step-by-Step Instructions:
1.  **Analyze the Query**: Read the user's query carefully. Identify the user's core intent. Is it a simple social interaction, a request for factual information, a creative prompt, or a complex command?
2.  **Select Task Type**: Based on your analysis, choose the *single best* task type from the list below.
3.  **Construct JSON**: Create a JSON object with the specified keys. The `response` key should only be filled for `greeting` and `simple_chat`. For all other types, it MUST be `null`.

# Task Type Definitions & Examples:

## Type: `greeting`
- **Description**: Simple social interactions, hellos, goodbyes, thank yous. No information is requested.
- **Examples**:
  - "こんにちは" -> `{"type": "greeting", "query": "こんにちは", "response": "こんにちは！何かお手伝いしましょうか？"}`
  - "ありがとう" -> `{"type": "greeting", "query": "ありがとう", "response": "どういたしまして。"}`
  - "じゃあね" -> `{"type": "greeting", "query": "じゃあね", "response": "はい、またお話ししましょう！"}`

## Type: `simple_chat`
- **Description**: Simple questions that do not require external tools or complex planning. Usually about you (the AI).
- **Examples**:
  - "あなたの名前は？" -> `{"type": "simple_chat", "query": "あなたの名前は？", "response": "私はHiPLEというAIです。"}`
  - "何ができるの？" -> `{"type": "simple_chat", "query": "何ができるの？", "response": "私は様々なタスクを計画し、エキスパートAIを実行することができます。"}`

## Type: `wikipedia`
- **Description**: Requests for established, encyclopedic facts about specific entities (people, places, historical events, scientific concepts).
- **Examples**:
  - "徳川家康について" -> `{"type": "wikipedia", "query": "徳川家康", "response": null}`
  - "量子力学とは" -> `{"type": "wikipedia", "query": "量子力学", "response": null}`

## Type: `web_search`
- **Description**: Requests for current, dynamic, or real-world information (news, weather, prices, reviews, recipes).
- **Examples**:
  - "今日のニュースを教えて" -> `{"type": "web_search", "query": "今日のニュース", "response": null}`
  - "iPhone 15のレビュー" -> `{"type": "web_search", "query": "iPhone 15 レビュー", "response": null}`
  - "アイスクリームの作り方" -> `{"type": "web_search", "query": "アイスクリームの作り方", "response": null}`

## Type: `complex_task`
- **Description**: Any request that requires multiple steps, planning, logical reasoning, or combining information from multiple sources. If a query doesn't fit neatly into other categories, it's likely a complex task.
- **Examples**:
  - "日本の少子高齢化問題についてレポートを書いて" -> `{"type": "complex_task", "query": "日本の少子高齢化問題についてレポートを書く", "response": null}`
  - "来週の福岡旅行のプランを立てて" -> `{"type": "complex_task", "query": "来週の福岡旅行のプランを立てる", "response": null}`

## Type: `emergent_task`
- **Description**: Creative, philosophical, or open-ended brainstorming prompts.
- **Examples**:
  - "新しいAIアシスタントの名前を5つ考えて" -> `{"type": "emergent_task", "query": "新しいAIアシスタントの名前を5つ考える", "response": null}`
  - "幸福とは何か、詩で表現して" -> `{"type": "emergent_task", "query": "幸福を詩で表現する", "response": null}`

# Final Output Format (JSON ONLY):
You must respond with only the JSON object. Do not add any explanatory text before or after the JSON.
{
  "type": "...",
  "query": "...",
  "response": ...
}
"""

    def _parse_routing_decision(self, raw_response: str, original_prompt: str) -> Dict[str, Any]:
        """
        LLMからの応答をパースして、ルーティング決定の辞書を返す。
        """
        try:
            # 正規表現でJSON部分を抽出
            json_match = re.search(r'\{[\s\S]*\}', raw_response)
            if json_match:
                json_str = json_match.group(0)
                data = json.loads(json_str)
                # 必須キーの存在をチェック
                if "type" in data and "query" in data:
                    return {
                        "type": data["type"],
                        "query": data["query"],
                        "response": data.get("response")
                    }
        except (json.JSONDecodeError, KeyError):
            # パースに失敗した場合は、常にcomplex_taskとしてフォールバック
            pass

        return {
            "type": "complex_task",
            "query": original_prompt,
            "response": None
        }

