# path: ./container/container.py
# title: DI Container with Tool-Use Agents
# description: WikipediaAgentとToolRouterAgentをDIコンテナに追加する。

from dependency_injector import containers, providers
from domain.model_manager import ModelManager
from services.model_loader import ModelLoaderService
from services.vectorization_service import VectorizationService
from services.retrieval_service import RetrievalService
from services.worker_manager import WorkerManagerService
from services.plan_evaluation_service import PlanEvaluationService
from orchestrator.hiple_orchestrator import HipleOrchestrator
from agents.planner_agent import PlannerAgent
from agents.generator_agent import GeneratorAgent
from agents.reporter_agent import ReporterAgent
from agents.consultant_agent import ConsultantAgent
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from agents.tool_router_agent import ToolRouterAgent
from agents.wikipedia_agent import WikipediaAgent
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

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
    worker_manager = providers.Singleton(WorkerManagerService)
    plan_evaluation_service = providers.Singleton(
        PlanEvaluationService,
        vectorization_service=vectorization_service
    )
    
    model_manager = providers.Singleton(
        ModelManager,
        config_path=config_path.model_config_path
    )
    
    # --- Agents (Engines) ---
    planner_agent = providers.Factory(
        PlannerAgent,
        model_loader=model_loader
    )
    
    consultant_agent = providers.Factory(
        ConsultantAgent,
        model_loader=model_loader
    )

    generator_agent = providers.Factory(
        GeneratorAgent,
        model_loader=model_loader,
        worker_manager=worker_manager,
        consultant_agent=consultant_agent
    )
    
    reporter_agent = providers.Factory(
        ReporterAgent,
        model_loader=model_loader
    )
    
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    tool_router_agent = providers.Factory(
        ToolRouterAgent,
        model_loader=model_loader
    )

    wikipedia_agent = providers.Factory(
        WikipediaAgent,
        model_loader=model_loader # 引数は必須だが実際には使われない
    )
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    # --- Orchestrator ---
    hiple_orchestrator = providers.Factory(
        HipleOrchestrator,
        model_manager=model_manager,
        planner_agent=planner_agent,
        generator_agent=generator_agent,
        reporter_agent=reporter_agent,
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        tool_router_agent=tool_router_agent,
        wikipedia_agent=wikipedia_agent,
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        retrieval_service=retrieval_service,
        plan_evaluation_service=plan_evaluation_service
    )