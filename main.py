# path: ./main.py
# title: Main Entry Point for HiPLE System
# description: HiPLEシステムを起動するメインファイル。TOKENIZERS_PARALLELISMを無効化。

import readline
import sys
import os
from container.container import Container
from orchestrator.hiple_orchestrator import HipleOrchestrator
from utils.monitoring import print_memory_usage

# huggingface/tokenizers の警告を抑制し、デッドロックのリスクを低減
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def main() -> None:
    """
    メイン関数
    """
    print("--- HiPLE (Hierarchical Predictive Language Engine) を初期化しています ---")
    print_memory_usage("INITIALIZING")
    try:
        container = Container()
        container.config_path.from_dict({
            'model_config_path': './config/models.yml'
        })
        
        orchestrator: HipleOrchestrator = container.hiple_orchestrator()

    except Exception as e:
        print(f"❌ エラー: 初期化に失敗しました。 - {e}")
        import traceback
        traceback.print_exc()
        print("設定ファイル(models.yml, .env)やモデルのパスを確認してください。")
        return

    print("--- 初期化が完了しました ---")
    print("対話を開始します。終了するには 'exit' または 'quit' と入力してください。")

    while True:
        try:
            question: str = input("> ")

            if question.lower() in ["exit", "quit"]:
                print("システムを終了します。")
                break

            if not question.strip():
                continue

            print("\n--- 思考中... ---")
            response: str = orchestrator.process_task(question)
            print("\n--- 回答 ---")
            print(response)
            print("\n")

        except KeyboardInterrupt:
            print("\nシステムを終了します。")
            break
        except Exception as e:
            print(f"致命的なエラーが発生しました: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()