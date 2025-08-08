# path: ./services/worker_manager.py
# title: External Worker Manager Service with Robust IPC
# description: プロセス間通信をより堅牢にするため、バイナリでデータを受け取り、明示的にUTF-8でデコードする。

import sys
import json
import subprocess
import traceback
from typing import List, Any, Dict, cast
from domain.schemas import ExpertModel
from llama_cpp.llama_types import ChatCompletionRequestMessage
import torch
from diffusers import DiffusionPipeline, AutoencoderKL

class WorkerExecutionError(Exception):
    """ワーカープロセスの実行エラー"""
    pass

class WorkerManagerService:
    """
    外部ワーカープロセスを呼び出し、LLMや拡散モデルの推論を実行するサービス
    """
    def invoke_llm_worker(self, expert: ExpertModel, messages: List[ChatCompletionRequestMessage]) -> Dict[str, Any]:
        """
        LLMワーカーをサブプロセスとして実行し、結果を返す
        """
        if not expert.model_path:
            raise ValueError(f"エキスパート '{expert.name}' に model_path が設定されていません。")

        payload = {
            "model_path": expert.model_path,
            "messages": messages,
            "chat_format": expert.chat_format,
        }

        try:
            python_executable = sys.executable
            timeout_seconds = 180 

            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            process = subprocess.run(
                [python_executable, "-m", "agents.worker"],
                input=json.dumps(payload, ensure_ascii=False).encode('utf-8'), # 明示的にUTF-8でエンコード
                capture_output=True,
                check=True,
                timeout=timeout_seconds
                # text=True と encoding='utf-8' を削除し、バイナリでやり取りする
            )
            
            # ワーカーからの標準出力をUTF-8でデコードしてからJSONとしてパース
            response_str = process.stdout.decode('utf-8')
            response_data = cast(Dict[str, Any], json.loads(response_str))
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            
            if "error" in response_data:
                raise WorkerExecutionError(f"ワーカープロセスでエラーが発生しました: {response_data['error']}\nTrace: {response_data.get('traceback', '')}")

            return response_data
        
        except subprocess.TimeoutExpired:
            raise WorkerExecutionError(
                f"思考エンジンの応答がタイムアウトしました ({timeout_seconds}秒)。"
                "エンジンがハングアップした可能性があります。"
                "詳細はプロジェクト内の logs/worker.log ファイルを確認してください。"
            )
        except FileNotFoundError:
            raise WorkerExecutionError(f"ワーカープロセス '{python_executable} -m agents.worker' を実行できません。パスを確認してください。")
        except subprocess.CalledProcessError as e:
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            # エラー出力もデコードして表示
            stderr_str = e.stderr.decode('utf-8') if e.stderr else "No stderr"
            raise WorkerExecutionError(f"ワーカープロセスの実行に失敗しました。\nStderr: {stderr_str}")
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        except json.JSONDecodeError as e:
            raise WorkerExecutionError(f"ワーカーからの応答がJSON形式ではありませんでした。Raw output: {e.doc}")
        except Exception as e:
            raise WorkerExecutionError(f"ワーカー管理中に予期せぬエラーが発生しました: {e}")

    def invoke_diffusion_worker(self, expert: ExpertModel, prompt: str) -> Any:
        """
        拡散モデルを直接ロードして実行（こちらは比較的安定しているためプロセス分離しない）
        """
        if not expert.model_id:
            raise ValueError("拡散モデルのmodel_idが設定されていません。")
        
        try:
            device = "cpu"
            if torch.backends.mps.is_available(): device = "mps"
            elif torch.cuda.is_available(): device = "cuda"
            
            vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16)
            pipe = DiffusionPipeline.from_pretrained(
                expert.model_id, vae=vae, torch_dtype=torch.float16, variant="fp16", use_safetensors=True
            )
            pipe = pipe.to(device)
            
            image = pipe(prompt=prompt).images[0]
            return image
        except Exception as e:
            print(f"❌ 拡散モデルの実行中にエラーが発生しました: {e}")
            traceback.print_exc()
            raise