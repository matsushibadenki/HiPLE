# path: ./container/container.py
# title: DI Container with Simple Router
# description: DIコンテナを更新し、LLMベースのToolRouterAgentを廃止して、新しいSimpleRouterを使用する。

from dependency_injector import containers, providers
from domain.model_manager import ModelManager
from services.model_loader import ModelLoaderService
from services.vectorization_service import VectorizationService
from services.worker_manager import WorkerManagerService
from services.plan_evaluation_service import PlanEvaluationService
from services.performance_tracker_service import PerformanceTrackerService
from services.rag_manager_service import RAGManagerService
from services.web_browser_service import WebBrowserService
from rag.retrievers import FaissRetriever
from orchestrator.hiple_orchestrator import HipleOrchestrator
from orchestrator.router import SimpleRouter
from agents.planner_agent import PlannerAgent
from agents.generator_agent import GeneratorAgent
from agents.reporter_agent import ReporterAgent
from agents.consultant_agent import ConsultantAgent
from agents.wikipedia_agent import WikipediaAgent
from agents.web_browser_agent import WebBrowserAgent
from agents.rag_agent import RAGAgent
from agents.reviewer_agent import ReviewerAgent

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
    web_browser_service = providers.Singleton(WebBrowserService)
    plan_evaluation_service = providers.Singleton(
        PlanEvaluationService,
        vectorization_service=vectorization_service
    )
    
    # RAG Components
    faiss_retriever = providers.Factory(
        FaissRetriever,
        vectorization_service=vectorization_service
    )

    rag_manager = providers.Singleton(
        RAGManagerService,
        vectorization_service=vectorization_service
    )

    model_manager = providers.Singleton(
        ModelManager,
        config_path=config_path.model_config_path
    )
    
    # --- Router ---
    simple_router = providers.Factory(SimpleRouter)

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
    
    wikipedia_agent = providers.Factory(
        WikipediaAgent,
        model_loader=model_loader
    )

    web_browser_agent = providers.Factory(
        WebBrowserAgent,
        model_loader=model_loader
    )

    rag_agent = providers.Factory(
        RAGAgent,
        model_loader=model_loader
    )

    reviewer_agent = providers.Factory(
        ReviewerAgent,
        model_loader=model_loader
    )

    # --- Orchestrator ---
    hiple_orchestrator = providers.Factory(
        HipleOrchestrator,
        model_manager=model_manager,
        simple_router=simple_router,
        planner_agent=planner_agent,
        generator_agent=generator_agent,
        reporter_agent=reporter_agent,
        wikipedia_agent=wikipedia_agent,
        web_browser_agent=web_browser_agent,
        web_browser_service=web_browser_service,
        reviewer_agent=reviewer_agent,
        plan_evaluation_service=plan_evaluation_service,
        performance_tracker=performance_tracker,
        rag_agent=rag_agent,
        rag_manager=rag_manager,
        faiss_retriever=faiss_retriever
    )
