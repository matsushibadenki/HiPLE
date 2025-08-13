# path: ./orchestrator/hiple_orchestrator.py
# title: Orchestrator with Modular RAG Integration
# description: Modular RAGのコンポーネントを統合し、動的な検索と生成を実行するオーケストレーター。

import time
import traceback
from typing import Dict, List, Tuple, Any, Optional
from domain.model_manager import ModelManager
from domain.schemas import SubTask, Plan, ExpertModel, Milestone
from agents.planner_agent import PlannerAgent
from agents.generator_agent import GeneratorAgent
from agents.reporter_agent import ReporterAgent
from agents.tool_router_agent import ToolRouterAgent
from agents.wikipedia_agent import WikipediaAgent
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from agents.rag_agent import RAGAgent
from services.rag_manager_service import RAGManagerService
from rag.retrievers import BaseRetriever
from rag.data_sources import PlanDataSource, Document
# ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
from services.plan_evaluation_service import PlanEvaluationService
from services.performance_tracker_service import PerformanceTrackerService

class HipleOrchestrator:
    """
    HiPLEアーキテクチャに基づき、思考プロセス全体を管理する。
    Modular RAGと動的なエキスパート選択を備える。
    """
    def __init__(
        self,
        model_manager: ModelManager,
        planner_agent: PlannerAgent,
        generator_agent: GeneratorAgent,
        reporter_agent: ReporterAgent,
        tool_router_agent: ToolRouterAgent,
        wikipedia_agent: WikipediaAgent,
        plan_evaluation_service: PlanEvaluationService,
        performance_tracker: PerformanceTrackerService,
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        rag_agent: RAGAgent,
        rag_manager: RAGManagerService,
        faiss_retriever: BaseRetriever, # 具体的なRetrieverをDI
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
    ):
        self.model_manager = model_manager
        self.planner_agent = planner_agent
        self.generator_agent = generator_agent
        self.reporter_agent = reporter_agent
        self.tool_router_agent = tool_router_agent
        self.wikipedia_agent = wikipedia_agent
        self.plan_evaluation_service = plan_evaluation_service
        self.performance_tracker = performance_tracker
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        self.rag_agent = rag_agent
        self.rag_manager = rag_manager
        # RAG Managerにリトリーバーを登録
        self.rag_manager.register_retriever("plan_retriever", faiss_retriever)
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        self.max_replanning_attempts = 2

    def process_task(self, prompt: str) -> str:
        if prompt.strip().lower() == "show performance":
            return self.performance_tracker.get_performance_summary()
            
        print(f"▶️ HiPLEタスク開始: {prompt}")
        try:
            active_experts = self.model_manager.get_all_experts()
            if not active_experts: return "エラー: 利用可能なエキスパートがいません。"

            print("\n--- Phase 0: Routing ---")
            routing_result = self.tool_router_agent.execute(prompt, active_experts)
            task_type = routing_result.get("tool", "no_tool")
            query = routing_result.get("query", prompt)

            print(f"🧠 ルーティング結果: {task_type.upper()}")
            if task_type in ["wikipedia", "web_search"]:
                print(f"🔑 抽出されたクエリ: '{query}'")

            if task_type == "wikipedia":
                return self.wikipedia_agent.execute(query)
            elif task_type == "web_search":
                return "ウェブ検索機能は現在実装中です。"
            elif task_type == "no_tool":
                return self._process_simple_task(prompt, active_experts)
            else: # complex_task
                return self._process_complex_task(prompt, active_experts)

        except Exception as e:
            traceback.print_exc()
            return f"致命的なエラーが発生しました: {e}"

    def _process_simple_task(self, prompt: str, experts: List[ExpertModel]) -> str:
        print("\n--- Dynamic Generation for Simple Task ---")
        expert = self.performance_tracker.get_best_expert(experts, task_type="simple_task")
        if not expert:
            return "エラー: 単純応答用のエキスパートが見つかりません。"
        
        expert.system_prompt = "あなたは、ユーザーの質問に誠実かつ簡潔に答える、優秀なAIアシスタントです。"
        
        task = SubTask(
            task_id=1,
            description=prompt,
            expert_name=expert.name,
            ssv_description=prompt,
            consultation_experts=[]
        )
        context = self._build_minimal_context(prompt)

        start_time = time.time()
        result = self.generator_agent.execute(task, expert, context, experts)
        execution_time = time.time() - start_time
        
        success = bool(result) and "エラー" not in result
        self.performance_tracker.update_performance(expert.name, execution_time, success)

        return result

    def _process_complex_task(self, prompt: str, experts: List[ExpertModel]) -> str:
        failed_plan: Optional[Plan] = None
        validation_error: Optional[str] = None

        for attempt in range(self.max_replanning_attempts):
            print(f"\n--- Phase 1: Hierarchical Planning (Attempt {attempt + 1}) ---")
            performance_summary = self.performance_tracker.get_performance_summary()
            current_plan = self.planner_agent.execute(
                prompt, experts, failed_plan, validation_error, performance_summary
            )

            print(f"L1 (Goal): {current_plan.overall_goal}")
            for m in current_plan.milestones:
                print(f"L2 (Milestone {m.milestone_id}): {m.title}")

            is_struct_valid, struct_error = self._validate_plan_structure(current_plan, experts)
            if not is_struct_valid:
                print(f"⚠️ 計画の構造検証に失敗: {struct_error}")
                validation_error = f"構造的エラー: {struct_error}"
                failed_plan = current_plan
                continue

            print("✅ 計画の構造は妥当です。")

            is_semantic_valid, semantic_error = self.plan_evaluation_service.check_semantic_coherence(current_plan.tasks)
            if not is_semantic_valid:
                print(f"⚠️ 計画の意味的一貫性検証に失敗: {semantic_error}")
                validation_error = f"意味的一貫性エラー: {semantic_error}"
                failed_plan = current_plan
                continue

            print("✅ 計画の意味的一貫性は妥当です。")

            return self._execute_plan(current_plan, experts)

        print(f"❌ {self.max_replanning_attempts}回の再計画の試行後も、有効な計画を作成できませんでした。")
        return "エラー: 実行可能な計画を立案できませんでした。プロンプトを具体的にして再度お試しください。"

    def _execute_plan(self, plan: Plan, experts: List[ExpertModel]) -> str:
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # Plan-level RAG Indexing
        print("\n--- Phase 2a: Modular RAG Indexing ---")
        plan_data_source = PlanDataSource(plan)
        self.rag_manager.build_index_from_source("plan_retriever", plan_data_source)
        
        print("\n--- Phase 2b: Context-Aware Generation (HiPLE-G) ---")
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        completed_tasks: Dict[int, SubTask] = {}
        worker_tasks = [t for t in plan.tasks if t.expert_name.lower() != 'reporter']

        while len(completed_tasks) < len(worker_tasks):
            executable_tasks = [t for t in worker_tasks if t.status == "pending" and all(d in completed_tasks for d in t.dependencies)]

            if not executable_tasks:
                if len(completed_tasks) < len(worker_tasks):
                    for task in worker_tasks:
                        if task.status != "completed":
                            expert = self.model_manager.get_expert(task.expert_name)
                            if expert:
                                self.performance_tracker.update_performance(expert.name, 0, False)
                    return "エラー: タスクの依存関係が循環しているか、計画に問題があります。"
                break

            for task in executable_tasks:
                expert = self.model_manager.get_expert(task.expert_name)
                if not expert:
                    task.result = f"エラー: エキスパート '{task.expert_name}' が見つかりませんでした。"
                    task.status = "failed"
                    completed_tasks[task.task_id] = task
                    continue

                # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
                # Task-level RAG Retrieval
                rag_decision = self.rag_agent.execute(task.ssv_description, experts)
                rag_results: List[Document] = []
                if rag_decision.get("needs_retrieval"):
                    query = rag_decision.get("query", task.ssv_description)
                    print(f"🔍 RAG検索を実行します (Query: '{query}')")
                    rag_results = self.rag_manager.query("plan_retriever", query, k=3)
                
                context = self._build_context_for_task(task, plan, completed_tasks, rag_results)
                # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️

                print(f"\n▶️ Executing Task {task.task_id} ({task.expert_name.upper()}): {task.description}")
                task.status = "in_progress"
                
                start_time = time.time()
                task.result = self.generator_agent.execute(task, expert, context, experts)
                execution_time = time.time() - start_time

                success = bool(task.result) and "エラー" not in task.result
                self.performance_tracker.update_performance(expert.name, execution_time, success)

                task.status = "completed" if success else "failed"
                completed_tasks[task.task_id] = task
                print(f"✅ Task {task.task_id} Completed. (Status: {task.status})")
                
                if not success:
                    break
            
            if any(t.status == "failed" for t in completed_tasks.values()):
                print("❌ 計画の実行中にタスクが失敗しました。処理を中断します。")
                break

        reporter_tasks = [t for t in plan.tasks if t.expert_name.lower() == 'reporter']
        if reporter_tasks:
             print("\n--- Phase 3: Reporting ---")
             final_report = self.reporter_agent.execute(plan, experts)
             return final_report
        else:
            if not completed_tasks: return "タスクは実行されましたが、結果がありませんでした。"
            succeeded_tasks = [t for t in completed_tasks.values() if t.status == "completed"]
            if succeeded_tasks:
                last_task = max(succeeded_tasks, key=lambda t: t.task_id)
                return last_task.result or "完了しましたが結果がありません。"
            else:
                return "エラー: 全てのタスクが失敗しました。"

    def _validate_plan_structure(self, plan: Plan, experts: List[ExpertModel]) -> Tuple[bool, str]:
        if not plan.tasks: return False, "計画にタスクが含まれていません。"
        task_ids = {task.task_id for task in plan.tasks}
        milestone_ids = {m.milestone_id for m in plan.milestones}
        valid_expert_names = {expert.name.lower() for expert in experts}

        for task in plan.tasks:
            if task.expert_name.lower() not in valid_expert_names:
                return False, f"タスク {task.task_id} のエキスパート '{task.expert_name}' が不正です。"
            if task.milestone_id is not None and task.milestone_id not in milestone_ids:
                 return False, f"タスク {task.task_id} のマイルストーンID '{task.milestone_id}' が不正です。"
            for dep_id in task.dependencies:
                if dep_id not in task_ids:
                    return False, f"タスク {task.task_id} の依存先 {dep_id} が不正です。"
        return True, "計画は構造的に妥当です。"

    def _build_context_for_task(self, task: SubTask, plan: Plan, completed_tasks: Dict[int, SubTask], rag_results: List[Document]) -> Dict[str, Any]:
        current_milestone = next((m for m in plan.milestones if m.milestone_id == task.milestone_id), None)
        dependency_results = ""
        if task.dependencies:
            for dep_id in sorted(task.dependencies):
                if dep_id in completed_tasks and completed_tasks[dep_id].status == "completed":
                    result = completed_tasks[dep_id].result
                    dependency_results += f"【先行タスク{dep_id}の結果】:\n{result}\n\n"
        
        return {
            "original_prompt": plan.original_prompt,
            "overall_goal": plan.overall_goal,
            "milestone": current_milestone,
            "ssv_description": task.ssv_description,
            "dependency_results": dependency_results,
            "rag_results": [doc.content for doc in rag_results] # 修正: contentのリストを渡す
        }

    def _build_minimal_context(self, prompt: str) -> Dict[str, Any]:
        return {
            "original_prompt": prompt,
            "overall_goal": prompt,
            "milestone": Milestone(milestone_id=1, title="Direct Task", description=prompt),
            "dependency_results": "",
            "rag_results": []
        }
