# path: ./utils/thought_logger.py
# title: Thought Process Logger
# description: Formats and displays the thought process stored in the GlobalWorkspace.

from typing import List, Dict, Any

class ThoughtLogger:
    """
    思考プロセスを人間が読みやすい形式で表示するためのクラス
    """

    @staticmethod
    def format_thoughts(thought_process: List[Dict[str, Any]]) -> str:
        """
        思考プロセスのリストを整形された文字列に変換する
        """
        if not thought_process:
            return "思考の記録はありません。"

        formatted_lines = ["# HiPLE Thought Process Log"]
        
        for i, thought in enumerate(thought_process):
            source = thought.get("source", "Unknown")
            thought_type = thought.get("type", "Generic")
            content = thought.get("content", "")

            header = f"\n--- Step {i+1}: [{source.upper()}] - {thought_type.replace('_', ' ').title()} ---"
            formatted_lines.append(header)

            if isinstance(content, dict):
                for key, value in content.items():
                    # Noneや空のリストは表示しない
                    if value is not None and value != []:
                        formatted_lines.append(f"  - {key.replace('_', ' ').title()}: {value}")
            elif isinstance(content, list):
                 for item in content:
                    formatted_lines.append(f"  - {item}")
            else:
                content_str = str(content)
                if len(content_str) > 150:
                    indented_content = "\n".join(["    " + line for line in content_str.splitlines()])
                    formatted_lines.append(f"  Content:\n{indented_content}")
                else:
                    formatted_lines.append(f"  {content_str}")

        return "\n".join(formatted_lines)