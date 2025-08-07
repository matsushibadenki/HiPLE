# path: ./services/model_loader.py
# title: Model Loader Service with Stabilized Parameters
# description: jamba_test.pyの設定を参考に、モデルロード時のパラメータを安定化させる。

import os
import gc
import sys
import traceback
from typing import Optional, Any, Union
import psutil
from llama_cpp import Llama
from domain.schemas import ExpertModel
import torch
from diffusers import DiffusionPipeline, AutoencoderKL
from utils.monitoring import print_memory_usage

class ModelLoaderService:
    """
    エキスパートモデルのロードとアンロード（スワッピング）を管理する
    """
    def __init__(self, memory_threshold_gb: int = 2) -> None:
        self.currently_loaded_expert: Optional[ExpertModel] = None
        self.memory_threshold_bytes = memory_threshold_gb * 1024 * 1024 * 1024

    def _check_memory(self) -> None:
        available_memory = psutil.virtual_memory().available
        if available_memory < self.memory_threshold_bytes:
            raise MemoryError(f"利用可能なメモリ ({available_memory / (1024**3):.2f}GB) が閾値を下回っています。")
        print(f"✅ メモリチェックOK (Available: {available_memory / (1024**3):.2f}GB)")

    def load_expert(self, expert: ExpertModel) -> Union[Llama, DiffusionPipeline]:
        if expert.is_loaded and expert.instance:
            if self.currently_loaded_expert and self.currently_loaded_expert.name != expert.name:
                self.unload_expert(self.currently_loaded_expert)
            self.currently_loaded_expert = expert
            print(f"✅ エキスパート '{expert.name}' は既にロード済みです。")
            if isinstance(expert.instance, Llama):
                expert.instance.reset()
            return expert.instance

        if self.currently_loaded_expert:
            self.unload_expert(self.currently_loaded_expert)

        self._check_memory()
        print(f"🔄 エキスパート '{expert.name}' をロードします...")
        print_memory_usage(f"BEFORE_LOAD_{expert.name.upper()}")

        try:
            instance: Union[Llama, DiffusionPipeline]
            if expert.chat_format == "diffusion":
                if not expert.model_id: raise ValueError("拡散モデルのmodel_idが未設定")
                device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
                vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16)
                pipe = DiffusionPipeline.from_pretrained(expert.model_id, vae=vae, torch_dtype=torch.float16, variant="fp16", use_safetensors=True)
                instance = pipe.to(device)
            else:
                if not expert.model_path: raise ValueError("LLMのmodel_pathが未設定")
                log_verbose = os.getenv("LOG_VERBOSE", "False").lower() in ("true", "1", "t")
                is_apple_silicon = sys.platform == "darwin" and "arm64" in os.uname().machine
                n_gpu_layers = -1 if is_apple_silicon else 0
                
                # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
                # jamba_test.pyを参考に、安定動作するパラメータ設定に統一
                n_threads = psutil.cpu_count(logical=False)
                instance = Llama(
                    model_path=expert.model_path, 
                    n_gpu_layers=n_gpu_layers, 
                    n_ctx=4096, 
                    use_mlock=True, 
                    use_mmap=False, # メモリマップを無効化
                    n_threads=n_threads, # スレッド数を明示
                    verbose=log_verbose, 
                    chat_format=expert.chat_format
                )
                # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

            expert.instance = instance
            expert.is_loaded = True
            self.currently_loaded_expert = expert
            print(f"✅ エキスパート '{expert.name}' の準備が完了しました。")
            print_memory_usage(f"AFTER_LOAD_{expert.name.upper()}")
            return instance
        except Exception as e:
            print(f"❌ エキスパート '{expert.name}' のロード中にエラー: {e}")
            traceback.print_exc()
            raise

    def unload_expert(self, expert: Optional[ExpertModel]) -> None:
        if expert and expert.instance:
            print(f"🧹 エキスパート '{expert.name}' をアンロードしメモリを解放します。")
            print_memory_usage(f"BEFORE_UNLOAD_{expert.name.upper()}")
            del expert.instance
            expert.instance = None
            expert.is_loaded = False
            if self.currently_loaded_expert and self.currently_loaded_expert.name == expert.name:
                self.currently_loaded_expert = None
            gc.collect()
            if torch.backends.mps.is_available(): torch.mps.empty_cache()
            elif torch.cuda.is_available(): torch.cuda.empty_cache()
            print_memory_usage(f"AFTER_UNLOAD_{expert.name.upper()}")