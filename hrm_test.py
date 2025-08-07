# /hybrid_llm_system/hrm_test.py
# HRMモデルの動作を最小構成でテストするためのスクリプト (診断機能付き)

import sys
import os
import traceback
import psutil
from llama_cpp import Llama
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage
from utils.monitoring import print_memory_usage

def main() -> None:
    """
    HRMモデルの最小環境テストを実行するメイン関数
    """
    print("--- HRMモデルの最小環境テストを開始します ---")
    print_memory_usage("START")
    
    model_path: Optional[str] = None
    try:
        load_dotenv()
        model_path = os.getenv("HRM_MODEL_PATH")

        if not model_path:
            print("❌ エラー: .envファイルにHRM_MODEL_PATHが設定されていません。")
            return
            
        if not os.path.exists(model_path):
            print(f"❌ エラー: モデルファイルが見つかりません。パスを確認してください: {model_path}")
            return

        print(f"モデルパス: {model_path}")
        print_memory_usage("BEFORE_LOAD")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")
        is_apple_silicon = sys.platform == "darwin" and "arm64" in os.uname().machine
        n_gpu_layers = -1 if is_apple_silicon else 0
        n_threads = psutil.cpu_count(logical=False)
        
        llm = Llama(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_threads=n_threads,
            use_mmap=False,
            n_ctx=4096,
            verbose=log_verbose,
            chat_format="chatml"
        )
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        print_memory_usage("AFTER_LOAD")
        print("✅ モデルの初期化に成功しました。")

        messages: List[ChatCompletionRequestMessage] = [
            {"role": "system", "content": "You are a logical reasoner. Think step by step to solve the problem."},
            {"role": "user", "content": "There are three suspects, A, B, and C. A says 'B is the culprit.' B says 'C is the culprit.' C says 'I am not the culprit.' Only one person is telling the truth, and there is only one culprit. Who is the culprit? Please explain your reasoning step by step."}
        ]

        print("\n--- 応答を生成します... ---")
        
        response: Any = llm.create_chat_completion(
            messages=messages,
            max_tokens=1024,
            temperature=0.2
        )
        
        print("\n--- 応答の生成に成功しました！ ---")

        if "choices" in response and response["choices"]:
            choice = response["choices"][0]
            if "message" in choice and "content" in choice["message"]:
                content: Optional[str] = choice["message"]["content"]
                if content is not None:
                    print("\n[モデルからの応答]")
                    print(content.strip())
                else:
                    print("応答メッセージにテキストが含まれていません。")
            else:
                print("応答メッセージの形式が正しくありません。")
        else:
            print("応答内容が空か、予期しない形式です。")
            print(f"受信したデータ: {response}")

    except Exception as e:
        print(f"\n❌ テスト中に予期せぬエラーが発生しました: {e}")
        traceback.print_exc()

    print("\n--- テストを終了します ---")
    print_memory_usage("END")

if __name__ == "__main__":
    main()