# /hybrid_llm_system/visualizer_test.py
# 拡散モデル(Stable Diffusion)の動作を最小構成でテストするスクリプト

import os
import torch
from dotenv import load_dotenv
from diffusers import DiffusionPipeline, AutoencoderKL
from typing import Optional

def main() -> None:
    """
    拡散モデルの最小環境テストを実行するメイン関数
    """
    print("--- 拡散モデル(Stable Diffusion)の最小環境テストを開始します ---")
    
    try:
        load_dotenv()
        # .envファイルからHugging FaceのモデルIDを取得
        model_id: Optional[str] = os.getenv("VISUALIZER_MODEL_ID")

        if not model_id or not model_id.strip():
            print("❌ エラー: .envファイルにVISUALIZER_MODEL_IDが設定されていません。")
            print("   (例: VISUALIZER_MODEL_ID=\"stabilityai/stable-diffusion-xl-base-1.0\")")
            return
        
        # GGUFファイルパスが誤って設定されていないかチェック
        if ".gguf" in model_id.lower():
            print(f"❌ エラー: VISUALIZER_MODEL_IDにはGGUFファイルのパスではなく、Hugging FaceのリポジトリIDを設定してください。")
            print(f"   現在の値: {model_id}")
            print(f"   正しい例: \"stabilityai/stable-diffusion-xl-base-1.0\"")
            return

        print(f"Hugging Face モデルID: {model_id}")

        # デバイスの自動選択 (MPS > CUDA > CPU)
        device = "cpu"
        if torch.backends.mps.is_available():
            device = "mps"
        elif torch.cuda.is_available():
            device = "cuda"
        
        print(f"使用デバイス: {device}")

        # VAE (Variational Auto Encoder) を個別にロード
        # これにより、特定の環境での黒い画像が出力される問題を回避
        vae = AutoencoderKL.from_pretrained(
            "madebyollin/sdxl-vae-fp16-fix", 
            torch_dtype=torch.float16
        )

        # 拡散モデルのパイプラインを初期化
        # 'from_pretrained'はリポジトリIDを元にHugging Face Hubからモデルをダウンロードします
        pipe = DiffusionPipeline.from_pretrained(
            model_id,
            vae=vae,
            torch_dtype=torch.float16,
            variant="fp16",
            use_safetensors=True
        )
        pipe = pipe.to(device)
        
        print("✅ モデルの初期化に成功しました。")

        # 画像生成用のプロンプト
        prompt = "A cinematic shot of a baby raccoon wearing an intricate italian mafioso suit, saying 'oh no'."

        print(f"\n--- 以下のプロンプトで画像を生成します... ---\n{prompt}")
        
        # 画像を生成
        image = pipe(prompt=prompt).images[0]
        
        print("\n--- 画像の生成に成功しました！ ---")

        # 出力ディレクトリを作成
        output_dir = "output/images"
        os.makedirs(output_dir, exist_ok=True)
        
        # ファイルを保存
        output_path = os.path.join(output_dir, "visualizer_test_output.png")
        image.save(output_path)
        
        print(f"\n🖼️ 画像を保存しました: {os.path.abspath(output_path)}")

    except Exception as e:
        print(f"\n❌ テスト中に予期せぬエラーが発生しました: {e}")
        import traceback
        traceback.print_exc()

    print("\n--- テストを終了します ---")

if __name__ == "__main__":
    main()