# path: ./domain/model_manager.py
# title: ModelManager with Dynamic Model Assignment (Cost/Speed Aware)
# description: .envとmodels.ymlからエキスパートを動的に読み込む際に、コストと速度のスコアも反映させる。

import os
import yaml
from typing import Dict, List, Optional
from dotenv import load_dotenv
from .schemas import ExpertModel

class ModelManager:
    """
    models.ymlからエキスパートモデルの定義を読み込み、.envの指定に基づいて動的に割り当てるクラス
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

        all_definitions = config.get("worker_experts", {})
        
        expert_mapping_str = os.getenv("EXPERT_MAPPING")
        if not expert_mapping_str:
            raise ValueError(".envファイルにEXPERT_MAPPINGが設定されていません。")

        try:
            expert_mapping = dict(item.strip().split(':') for item in expert_mapping_str.split(','))
        except ValueError:
            raise ValueError("EXPERT_MAPPINGの形式が正しくありません。'type:definition, type:definition'の形式で記述してください。")

        loaded_experts: Dict[str, ExpertModel] = {}

        for expert_type, definition_key in expert_mapping.items():
            settings = all_definitions.get(definition_key)

            if not settings:
                print(f"⚠️ 警告: EXPERT_MAPPINGで指定された '{definition_key}' の定義がmodels.ymlに見つかりません。")
                continue

            if not settings.get("enabled", False):
                print(f"ℹ️ エキスパート '{definition_key}' は設定で無効化されています。スキップします。")
                continue
            
            is_diffusion_model = settings.get("chat_format") == "diffusion"
            model_path: Optional[str] = None
            model_id: Optional[str] = None

            if is_diffusion_model:
                model_id = settings.get("model_id")
            else:
                model_env_key = settings.get("model_env_key")
                if model_env_key:
                    model_path = os.getenv(model_env_key)
                
                if not model_path:
                    print(f"⚠️ 警告: エキスパート '{settings.get('name', definition_key)}' のモデルパス (環境変数: {model_env_key}) が見つかりません。スキップします。")
                    continue
            
            expert_name = settings.get("name", expert_type)
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
            loaded_experts[expert_name.lower()] = ExpertModel(
                name=expert_name,
                description=settings.get("description", ""),
                model_path=model_path,
                model_id=model_id,
                chat_format=settings.get("chat_format", "default"),
                system_prompt=settings.get("system_prompt", ""),
                execution_strategy=settings.get("execution_strategy", "inline"),
                keywords=settings.get("keywords", []),
                cost_score=settings.get("cost_score", 5),
                speed_score=settings.get("speed_score", 5),
                enabled=True
            )
            # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

        if not loaded_experts:
            raise ValueError("有効なエキスパートが一人も設定されていません。.envとmodels.ymlを確認してください。")
            
        return loaded_experts

    def get_expert(self, name: str) -> Optional[ExpertModel]:
        return self.experts.get(name.lower())

    def get_all_experts(self) -> List[ExpertModel]:
        return list(self.experts.values())