# path: ./agents/worker.py
# title: Stabilized External LLM Worker
# description: LLMの推論を独立したプロセスで実行するワーカー。安定化パラメータを適用。

import sys
import os
import json
import traceback
import logging
import psutil # 追加
from llama_cpp import Llama
from dotenv import load_dotenv
from pathlib import Path

log_dir = Path(__file__).resolve().parent.parent / "logs"
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "worker.log"
if log_file.exists():
    log_file.unlink()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(process)d - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(log_file, encoding='utf-8')]
)

def main() -> None:
    try:
        logging.info("--- Worker process started ---")
        
        input_data = json.load(sys.stdin)
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
        
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")
        is_apple_silicon = sys.platform == "darwin" and "arm64" in os.uname().machine
        n_gpu_layers = -1 if is_apple_silicon else 0
        n_threads = psutil.cpu_count(logical=False)

        llm = Llama(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_threads=n_threads,
            n_ctx=4096,
            use_mmap=False,
            use_mlock=True,
            verbose=log_verbose,
            chat_format=chat_format
        )
        
        logging.info("Llama model initialized successfully.")
        
        # ワーカーからの応答の多様性を確保するため、temperatureを少し上げる
        output = llm.create_chat_completion(
            messages=messages,
            max_tokens=4096,
            temperature=0.5,
            stop=["<|im_end|>", "</s>", "<|endoftext|>"]
        )
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        logging.info("Chat completion created successfully.")

        json.dump(output, sys.stdout)
        sys.stdout.flush()
        logging.info("--- Worker process finished successfully ---")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        error_info = {"error": str(e), "traceback": traceback.format_exc()}
        json.dump(error_info, sys.stdout)
        sys.stdout.flush()
        sys.exit(1)

if __name__ == "__main__":
    main()