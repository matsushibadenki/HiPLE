# path: ./container/container.py
# title: Finalized DI Container
# description: WorkerManagerServiceをGeneratorAgentに注入する最終設定。

from dependency_injector import containers, providers
from domain.model_manager import ModelManager
from services.model_loader import ModelLoaderService
from services.vectorization_service import VectorizationService
from services.retrieval_service import RetrievalService
from services.worker_manager import WorkerManagerService # 追加
from orchestrator.hiple_orchestrator import HipleOrchestrator
from agents.planner_agent import PlannerAgent
from agents.generator_agent import GeneratorAgent
from agents.reporter_agent import ReporterAgent
from agents.router_agent import RouterAgent

class Container(containers.DeclarativeContainer):
    """
    DIコンテナ
    アプリケーションの依存関係を管理します。
    """
    config_path = providers.Configuration()

    # --- Services ---
    model_loader = providers.Singleton(ModelLoaderService)
    vectorization_service = providers.Singleton(VectorizationService)
    retrieval_service = providers.Singleton(
        RetrievalService,
        vectorization_service=vectorization_service
    )
    worker_manager = providers.Singleton(WorkerManagerService) # 追加
    
    model_manager = providers.Singleton(
        ModelManager,
        config_path=config_path.model_config_path
    )
    
    # --- Agents (Engines) ---
    planner_agent = providers.Factory(
        PlannerAgent,
        model_loader=model_loader
    )
    
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    generator_agent = providers.Factory(
        GeneratorAgent,
        model_loader=model_loader,
        worker_manager=worker_manager # WorkerManagerを注入
    )
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    
    reporter_agent = providers.Factory(
        ReporterAgent,
        model_loader=model_loader
    )
    
    router_agent = providers.Factory(
        RouterAgent,
        model_loader=model_loader
    )

    # --- Orchestrator ---
    hiple_orchestrator = providers.Factory(
        HipleOrchestrator,
        model_manager=model_manager,
        planner_agent=planner_agent,
        generator_agent=generator_agent,
        reporter_agent=reporter_agent,
        router_agent=router_agent,
        retrieval_service=retrieval_service
    )