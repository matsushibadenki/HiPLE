# path: ./agents/worker.py
# title: Stabilized External LLM Worker with Robust IPC
# description: プロセス間通信をより堅牢にするため、標準出力にバイナリデータを書き込む。

import sys
import os
import json
import traceback
import logging
import psutil
from llama_cpp import Llama
from dotenv import load_dotenv
from pathlib import Path

# (logging設定は変更なし)
# ...

def main() -> None:
    try:
        logging.info("--- Worker process started ---")
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # 標準入力をバイナリで読み取り、UTF-8でデコード
        input_bytes = sys.stdin.buffer.read()
        input_data = json.loads(input_bytes.decode('utf-8'))
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        logging.info("Successfully read from stdin.")

        model_path = input_data.get("model_path")
        messages = input_data.get("messages")
        chat_format = input_data.get("chat_format")
        
        if not all([model_path, messages, chat_format]):
            raise ValueError("入力データに必須キーが不足しています。")

        logging.info(f"Model path: {model_path}")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"モデルファイルが見つかりません: {model_path}")

        load_dotenv()
        
        log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")
        is_apple_silicon = sys.platform == "darwin" and "arm64" in os.uname().machine
        n_gpu_layers = 0
        n_threads = psutil.cpu_count(logical=False)

        llm = Llama(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_threads=n_threads,
            n_ctx=4096,
            use_mmap=False,
            verbose=log_verbose,
            chat_format=chat_format
        )
        
        logging.info("Llama model initialized successfully.")
        
        output = llm.create_chat_completion(
            messages=messages,
            max_tokens=4096,
            temperature=0.7,
            stop=["<|im_end|>", "</s>", "<|endoftext|>"]
        )
        
        logging.info("Chat completion created successfully.")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # 結果をJSON文字列に変換し、UTF-8でエンコードして標準出力（バイナリモード）に書き込む
        output_str = json.dumps(output, ensure_ascii=False)
        sys.stdout.buffer.write(output_str.encode('utf-8'))
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        sys.stdout.flush()
        logging.info("--- Worker process finished successfully ---")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        error_info = {"error": str(e), "traceback": traceback.format_exc()}
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        error_str = json.dumps(error_info, ensure_ascii=False)
        sys.stdout.buffer.write(error_str.encode('utf-8'))
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        sys.stdout.flush()
        sys.exit(1)

if __name__ == "__main__":
    main()