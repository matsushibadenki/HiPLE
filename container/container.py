# path: ./container/container.py
# title: DI Container with Modular RAG Components
# description: DIコンテナにModular RAG関連のサービスとエージェントを登録する。

from dependency_injector import containers, providers
from domain.model_manager import ModelManager
from services.model_loader import ModelLoaderService
from services.vectorization_service import VectorizationService
from services.worker_manager import WorkerManagerService
from services.plan_evaluation_service import PlanEvaluationService
from services.performance_tracker_service import PerformanceTrackerService
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from services.rag_manager_service import RAGManagerService
from rag.retrievers import FaissRetriever
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from orchestrator.hiple_orchestrator import HipleOrchestrator
from agents.planner_agent import PlannerAgent
from agents.generator_agent import GeneratorAgent
from agents.reporter_agent import ReporterAgent
from agents.consultant_agent import ConsultantAgent
from agents.tool_router_agent import ToolRouterAgent
from agents.wikipedia_agent import WikipediaAgent
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from agents.rag_agent import RAGAgent
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
    performance_tracker = providers.Singleton(PerformanceTrackerService)
    worker_manager = providers.Singleton(WorkerManagerService)
    plan_evaluation_service = providers.Singleton(
        PlanEvaluationService,
        vectorization_service=vectorization_service
    )
    
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    # RAG Components
    faiss_retriever = providers.Factory(
        FaissRetriever,
        vectorization_service=vectorization_service
    )

    rag_manager = providers.Singleton(
        RAGManagerService,
        vectorization_service=vectorization_service
    )
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

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
    
    tool_router_agent = providers.Factory(
        ToolRouterAgent,
        model_loader=model_loader
    )

    wikipedia_agent = providers.Factory(
        WikipediaAgent,
        model_loader=model_loader
    )

    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    rag_agent = providers.Factory(
        RAGAgent,
        model_loader=model_loader
    )
    # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

    # --- Orchestrator ---
    hiple_orchestrator = providers.Factory(
        HipleOrchestrator,
        model_manager=model_manager,
        planner_agent=planner_agent,
        generator_agent=generator_agent,
        reporter_agent=reporter_agent,
        tool_router_agent=tool_router_agent,
        wikipedia_agent=wikipedia_agent,
        plan_evaluation_service=plan_evaluation_service,
        performance_tracker=performance_tracker,
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        rag_agent=rag_agent,
        rag_manager=rag_manager,
        faiss_retriever=faiss_retriever
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    )
