# /hybrid_llm_system/liquids4_test.py
# LiquidS4モデルの動作を最小構成でテストするためのスクリプト (mypy対応版)

import sys
import os
from llama_cpp import Llama
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
from llama_cpp.llama_types import ChatCompletionRequestMessage # 追加

def main() -> None:
    """
    LiquidS4モデルの最小環境テストを実行するメイン関数
    """
    print("--- LiquidS4モデルの最小環境テストを開始します ---")
    
    model_path: Optional[str] = None
    try:
        # .envファイルから環境変数を読み込み
        load_dotenv()
        model_path = os.getenv("LIQUIDS4_MODEL_PATH")

        if not model_path:
            print("🟡 テストをスキップ: .envファイルにLIQUIDS4_MODEL_PATHが設定されていません。")
            return
            
        if not os.path.exists(model_path):
            print(f"❌ エラー: モデルファイルが見つかりません。パスを確認してください: {model_path}")
            return

        print(f"モデルパス: {model_path}")

        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")

        # モデルの初期化 (llama-2フォーマット)
        llm = Llama(
            model_path=model_path,
            n_ctx=8192,
            n_gpu_layers=-1,
            verbose=log_verbose,
            chat_format="llama-2"
        )
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        print("✅ モデルの初期化に成功しました。")
        
        # チャット形式のプロンプトを作成
        long_text = """
        Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by humans and other animals. 
        Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. 
        Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".
        As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. 
        For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology.
        """
        messages: List[ChatCompletionRequestMessage] = [ # 型を修正
            {"role": "system", "content": "You are an expert in summarizing and analyzing long texts. Provide a clear, concise, and logical summary."},
            {"role": "user", "content": f"Please summarize the following text:\n\n{long_text}"}
        ]
        
        print("\n--- 応答を生成します... ---")
        
        # チャット補完APIを呼び出し
        response: Any = llm.create_chat_completion(
            messages=messages,
            max_tokens=512,
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

    print("\n--- テストを終了します ---")

if __name__ == "__main__":
    main()