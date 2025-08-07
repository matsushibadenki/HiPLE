# path: ./domain/model_manager.py
# title: ModelManager with Execution Strategy
# description: エキスパート定義の読み込み時に、実行戦略も読み込むようにする。

import os
import yaml
from typing import Dict, List, Optional
from dotenv import load_dotenv
from .schemas import ExpertModel

class ModelManager:
    """
    models.ymlからエキスパートモデルの定義を読み込み、管理するクラス
    """
    def __init__(self, config_path: str):
        load_dotenv()
        self.experts: Dict[str, ExpertModel] = self._load_experts_from_config(config_path)

    def _load_experts_from_config(self, config_path: str) -> Dict[str, ExpertModel]:
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"モデル設定ファイルが見つかりません: {config_path}")
        except Exception as e:
            raise RuntimeError(f"モデル設定ファイルの読み込みに失敗しました: {e}")

        experts: Dict[str, ExpertModel] = {}
        expert_definitions = config.get("worker_experts", {})

        for name, settings in expert_definitions.items():
            if not settings.get("enabled", False):
                print(f"ℹ️ エキスパート '{name}' は設定で無効化されています。スキップします。")
                continue

            is_diffusion_model = settings.get("chat_format") == "diffusion"
            model_path: Optional[str] = None
            model_id: Optional[str] = None

            if is_diffusion_model:
                model_id = settings.get("model_id")
            else:
                model_path_env_key = settings.get("model_path_env")
                if model_path_env_key:
                    model_path = os.getenv(model_path_env_key)
                
                if not model_path:
                    print(f"⚠️ 警告: エキスパート '{name}' のモデルパスが見つかりません。スキップします。")
                    continue
            
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            experts[name.lower()] = ExpertModel(
                name=settings.get("name", name),
                description=settings.get("description", ""),
                model_path=model_path,
                model_id=model_id,
                chat_format=settings.get("chat_format", "default"),
                system_prompt=settings.get("system_prompt", ""),
                execution_strategy=settings.get("execution_strategy", "inline"),
                keywords=settings.get("keywords", []),
                enabled=True
            )
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        if not experts:
            raise ValueError("有効なエキスパートが一人も設定されていません。.envとmodels.ymlを確認してください。")
            
        return experts

    def get_expert(self, name: str) -> Optional[ExpertModel]:
        return self.experts.get(name.lower())

    def get_all_experts(self) -> List[ExpertModel]:
        return list(self.experts.values())