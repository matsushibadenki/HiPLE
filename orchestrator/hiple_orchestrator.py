# path: ./orchestrator/hiple_orchestrator.py
# title: Orchestrator with Emergence Task Handling
# description: Integrates the EmergenceAgent to handle creative brainstorming tasks.

import time
import traceback
from typing import Dict, List, Tuple, Any, Optional, cast

from domain.model_manager import ModelManager
from domain.schemas import SubTask, Plan, ExpertModel, Milestone
from agents.planner_agent import PlannerAgent
from agents.generator_agent import GeneratorAgent
from agents.reporter_agent import ReporterAgent
from agents.critic_agent import CriticAgent
from agents.rag_agent import RAGAgent
from agents.reviewer_agent import ReviewerAgent
from agents.safety_director_agent import SafetyDirectorAgent
from agents.metacognition_agent import MetacognitionAgent
from agents.emergence_agent import EmergenceAgent
from services.evolution_service import EvolutionService
from services.rag_manager_service import RAGManagerService
from services.plan_evaluation_service import PlanEvaluationService
from services.performance_tracker_service import PerformanceTrackerService
from services.tool_manager_service import ToolManagerService
from rag.retrievers import BaseRetriever
from rag.data_sources import PlanDataSource, Document
from workspace.global_workspace import GlobalWorkspace
from utils.thought_logger import ThoughtLogger
from .router import SimpleRouter

class HipleOrchestrator:
    def __init__(
        self,
        model_manager: ModelManager,
        simple_router: SimpleRouter,
        planner_agent: PlannerAgent,
        generator_agent: GeneratorAgent,
        reporter_agent: ReporterAgent,
        reviewer_agent: ReviewerAgent,
        plan_evaluation_service: PlanEvaluationService,
        performance_tracker: PerformanceTrackerService,
        rag_agent: RAGAgent,
        rag_manager: RAGManagerService,
        faiss_retriever: BaseRetriever,
        critic_agent: CriticAgent,
        tool_manager: ToolManagerService,
        global_workspace: GlobalWorkspace,
        thought_logger: ThoughtLogger,
        safety_director_agent: SafetyDirectorAgent,
        metacognition_agent: MetacognitionAgent,
        evolution_service: EvolutionService,
        emergence_agent: EmergenceAgent
    ):
        self.model_manager = model_manager
        self.simple_router = simple_router
        self.planner_agent = planner_agent
        self.generator_agent = generator_agent
        self.reporter_agent = reporter_agent
        self.reviewer_agent = reviewer_agent
        self.plan_evaluation_service = plan_evaluation_service
        self.performance_tracker = performance_tracker
        self.rag_agent = rag_agent
        self.rag_manager = rag_manager
        self.rag_manager.register_retriever("plan_retriever", faiss_retriever)
        self.critic_agent = critic_agent
        self.tool_manager = tool_manager
        self.workspace = global_workspace
        self.thought_logger = thought_logger
        self.safety_director = safety_director_agent
        self.metacognition = metacognition_agent
        self.evolution_service = evolution_service
        self.emergence_agent = emergence_agent
        self.task_counter_for_evolution = 0
        self.evolution_check_interval = 3 # 3回の複雑なタスクごとに進化サイクルを実行
        self.max_replanning_attempts = 3
        self.max_feedback_loops = 2
        self.max_tool_uses_per_task = 3

    def process_task(self, prompt: str) -> str:
        if prompt.strip().lower() == "show performance":
            return self.performance_tracker.get_performance_summary()
        if prompt.strip().lower() == "show thoughts":
            return self.thought_logger.format_thoughts(self.workspace.thought_process)

        self.workspace.clear()
        self.workspace.set_initial_prompt(prompt)
        
        print(f"▶️ HiPLEタスク開始: {prompt}")
        try:
            active_experts = self.model_manager.get_all_experts()
            if not active_experts: return "エラー: 利用可能なエキスパートがいません。"

            self.workspace.add_thought("orchestrator", "routing_start", "Phase 0: Routing")
            route_result = self.simple_router.route(prompt)
            task_type = route_result["type"]
            self.workspace.add_thought("orchestrator", "routing_result", {"task_type": task_type, "query": route_result.get("query")})
            
            print(f"🧠 ルーティング結果: {task_type.upper()}")
            
            result = ""
            is_complex = False

            if task_type == "greeting":
                result = cast(str, route_result["response"])
            else:
                query = cast(str, route_result["query"])
                if task_type == "wikipedia":
                    result = self.tool_manager.execute_tool("wikipedia_search", query, "", active_experts)
                elif task_type == "web_search":
                    url = route_result.get("url", "")
                    if not url: return "ウェブ検索にはURLが必要です。"
                    result = self.tool_manager.execute_tool("web_search", query, url, active_experts)
                elif task_type == "simple_chat":
                    result = self._process_simple_task(query, active_experts)
                elif task_type == "emergent_task":
                    response_data = self.emergence_agent.execute(query, active_experts)
                    result = response_data.get("response", "創発的タスクの実行に失敗しました。")
                elif task_type == "complex_task":
                    result = self._process_complex_task(query, active_experts)
                    is_complex = True
                else:
                    result = f"エラー: 不明なタスクタイプ '{task_type}'"

            if is_complex:
                self.task_counter_for_evolution += 1
                if self.task_counter_for_evolution % self.evolution_check_interval == 0:
                    print("\n🔬 自己進化サイクルを実行しています...")
                    evolution_proposal = self.evolution_service.run_evolution_cycle()
                    if evolution_proposal:
                        result += "\n\n" + evolution_proposal
            return result

        except Exception as e:
            traceback.print_exc()
            self.workspace.add_thought("orchestrator", "fatal_error", {"error": str(e), "traceback": traceback.format_exc()})
            return f"致命的なエラーが発生しました: {e}"
        finally:
            self.tool_manager.web_browser_service.close_browser_sync()

    def _process_simple_task(self, prompt: str, experts: List[ExpertModel]) -> str:
        self.workspace.add_thought("orchestrator", "simple_task_start", "Dynamic Generation for Simple Task")
        expert = next((e for e in experts if e.name.lower() == "greeter"), None)
        if not expert:
            expert = self.performance_tracker.get_best_expert(experts, task_type="simple_task")
        
        if not expert:
            return "エラー: 単純応答用のエキスパートが見つかりません。"
        
        self.workspace.add_thought("orchestrator", "expert_selection", {"expert": expert.name, "reason": "Simple Chat"})
        
        task = SubTask(
            task_id=1,
            description=prompt,
            expert_name=expert.name,
            ssv_description=prompt,
        )
        context = self._build_minimal_context(prompt)

        start_time = time.time()
        response_dict = self.generator_agent.execute(task, expert, context, experts)
        result = cast(str, response_dict.get("result", "エラー: 応答がありません。"))
        execution_time = time.time() - start_time
        
        success = result is not None and result.strip() != "" and "エラー" not in result
        self.performance_tracker.update_performance(expert.name, execution_time, success)
        self.workspace.add_thought("orchestrator", "simple_task_end", {"result": result, "success": success, "self_evaluation": task.self_evaluation})

        return result


    def _process_complex_task(self, prompt: str, experts: List[ExpertModel]) -> str:
        failed_plan: Optional[Plan] = None
        validation_error: Optional[str] = None

        for attempt in range(self.max_replanning_attempts):
            safety_check_result = self.safety_director.review_thought_process(self.workspace)
            if safety_check_result and "Aborting" in safety_check_result:
                self.workspace.add_thought("safety_director", "intervention", {"reason": safety_check_result})
                return f"安全性エラー: {safety_check_result}"

            self.workspace.add_thought("orchestrator", "planning_start", f"Phase 1: Hierarchical Planning (Attempt {attempt + 1})")
            performance_summary = self.performance_tracker.get_performance_summary()
            
            current_plan = self.planner_agent.execute(
                prompt, experts, self.tool_manager, failed_plan, validation_error, performance_summary
            )
            self.workspace.add_thought("planner_agent", "plan_generated", {"goal": current_plan.overall_goal, "milestones": [m.title for m in current_plan.milestones], "task_count": len(current_plan.tasks)})

            is_executable, cognitive_load_msg = self.metacognition.analyze_cognitive_load(current_plan)
            if not is_executable:
                self.workspace.add_thought("metacognition_agent", "plan_rejected", {"reason": cognitive_load_msg})
                validation_error = cognitive_load_msg
                failed_plan = current_plan
                continue
            self.workspace.add_thought("metacognition_agent", "plan_approved", cognitive_load_msg)

            is_struct_valid, struct_error = self._validate_plan_structure(current_plan, experts)
            if not is_struct_valid:
                self.workspace.add_thought("orchestrator", "plan_validation_failed", {"reason": "Structural error", "error": struct_error})
                validation_error = f"構造的エラー: {struct_error}"
                failed_plan = current_plan
                continue

            self.workspace.add_thought("orchestrator", "plan_validation_succeeded", "Plan structure is valid.")

            is_semantic_valid, semantic_error = self.plan_evaluation_service.check_semantic_coherence(current_plan.tasks)
            if not is_semantic_valid:
                self.workspace.add_thought("orchestrator", "plan_validation_failed", {"reason": "Semantic coherence error", "error": semantic_error})
                validation_error = f"意味的一貫性エラー: {semantic_error}"
                failed_plan = current_plan
                continue

            self.workspace.add_thought("orchestrator", "plan_validation_succeeded", "Plan semantic coherence is valid.")

            self.workspace.add_thought("orchestrator", "critic_phase_start", "Phase 1c: Strategic Review by Critic Agent")
            critic_feedback = self.critic_agent.execute(current_plan, experts)

            if "計画に問題は見つかりませんでした。" not in critic_feedback:
                self.workspace.add_thought("critic_agent", "plan_criticism_received", {"feedback": critic_feedback})
                print(f"⚠️ 批評家からの指摘を受信: {critic_feedback}")
                validation_error = f"批評家からの指摘: {critic_feedback}"
                failed_plan = current_plan
                continue
            
            self.workspace.add_thought("critic_agent", "plan_approved", "The plan was approved by the critic.")
            print("✅ 計画は批評家によって承認されました。")

            return self._execute_plan(current_plan, experts)

        self.workspace.add_thought("orchestrator", "planning_failed", f"Failed to create a valid plan after {self.max_replanning_attempts} attempts.")
        return "エラー: 実行可能な計画を立案できませんでした。プロンプトを具体的にして再度お試しください。"

    def _execute_plan(self, plan: Plan, experts: List[ExpertModel]) -> str:
        self.workspace.add_thought("orchestrator", "execution_start", "Phase 2a: Modular RAG Indexing")
        plan_data_source = PlanDataSource(plan)
        self.rag_manager.build_index_from_source("plan_retriever", plan_data_source)
        
        self.workspace.add_thought("orchestrator", "execution_phase_start", "Phase 2b: Context-Aware Generation (HiPLE-G)")
        completed_tasks: Dict[int, SubTask] = {}
        worker_tasks = [t for t in plan.tasks if t.expert_name.lower() != 'reporter']

        while len(completed_tasks) < len(worker_tasks):
            safety_check_result = self.safety_director.review_thought_process(self.workspace)
            if safety_check_result and "Aborting" in safety_check_result:
                self.workspace.add_thought("safety_director", "intervention", {"reason": safety_check_result})
                return f"安全性エラー: {safety_check_result}"

            executable_tasks = [t for t in worker_tasks if t.status == "pending" and all(d in completed_tasks for d in t.dependencies)]

            if not executable_tasks:
                if len(completed_tasks) < len(worker_tasks):
                    for task in worker_tasks:
                        if task.status != "completed":
                            expert = self.model_manager.get_expert(task.expert_name)
                            if expert: self.performance_tracker.update_performance(expert.name, 0, False)
                    self.workspace.add_thought("orchestrator", "execution_error", "Circular dependency or dead-end in plan.")
                    return "エラー: タスクの依存関係が循環しているか、計画に問題があります。"
                break

            for task in executable_tasks:
                expert = self.model_manager.get_expert(task.expert_name)
                if not expert:
                    task.result = f"エラー: エキスパート '{task.expert_name}' が見つかりませんでした。"
                    task.status = "failed"
                    completed_tasks[task.task_id] = task
                    self.workspace.add_thought("orchestrator", "task_failed", {"task_id": task.task_id, "reason": f"Expert '{task.expert_name}' not found."})
                    continue

                execution_time = 0.0
                task_context: Dict[str, Any] = {}
                
                for loop_count in range(self.max_feedback_loops + self.max_tool_uses_per_task):
                    rag_decision_data = self.rag_agent.execute(task.ssv_description, experts)
                    rag_decision = cast(Dict[str, Any], rag_decision_data.get("response", {}))
                    rag_results: List[Document] = []
                    if isinstance(rag_decision, dict) and rag_decision.get("needs_retrieval"):
                        query = rag_decision.get("query", task.ssv_description)
                        rag_results = self.rag_manager.query("plan_retriever", query, k=3)
                        self.workspace.add_thought("rag_agent", "retrieval_performed", {"query": query, "results_count": len(rag_results)})
                    
                    current_context = self._build_context_for_task(task, plan, completed_tasks, rag_results, task_context.get("tool_results", ""))

                    self.workspace.add_thought("orchestrator", "task_execution_start", {"task_id": task.task_id, "expert": expert.name, "attempt": loop_count + 1, "description": task.description})
                    task.status = "in_progress"
                    
                    start_time = time.time()
                    response_dict = self.generator_agent.execute(task, expert, current_context, experts)
                    execution_time += time.time() - start_time

                    if response_dict.get("status") == "tool_request":
                        tool_name = response_dict.get("tool_name", "")
                        tool_query = response_dict.get("tool_query", "")
                        tool_url = response_dict.get("tool_url", "")
                        self.workspace.add_thought("generator_agent", "tool_request", {"tool_name": tool_name, "tool_query": tool_query})
                        
                        tool_result = self.tool_manager.execute_tool(tool_name, tool_query, tool_url, experts)
                        self.workspace.add_thought("tool_manager", "tool_result", {"tool_name": tool_name, "result_length": len(tool_result)})
                        
                        task_context["tool_results"] = tool_result
                        continue

                    generated_output = response_dict.get("result", "")

                    if task.reviewer_expert:
                        reviewer = self.model_manager.get_expert(task.reviewer_expert)
                        if reviewer:
                            self.workspace.add_thought("orchestrator", "review_start", {"task_id": task.task_id, "reviewer": reviewer.name})
                            feedback_data = self.reviewer_agent.execute(task, generated_output, reviewer, expert)
                            feedback = feedback_data.get("response", "")
                            if "修正の必要はありません" not in feedback and "問題ありません" not in feedback:
                                self.workspace.add_thought("reviewer_agent", "feedback_provided", {"task_id": task.task_id, "feedback": feedback})
                                task.feedback_history.append({"reviewer": reviewer.name, "feedback": feedback})
                                task_context["feedback"] = feedback
                                continue
                            self.workspace.add_thought("reviewer_agent", "review_passed", {"task_id": task.task_id})
                    
                    task.result = generated_output
                    break
                
                success = task.result is not None and task.result.strip() != "" and "エラー" not in task.result
                self.performance_tracker.update_performance(expert.name, execution_time, success)

                task.status = "completed" if success else "failed"
                completed_tasks[task.task_id] = task
                self.workspace.add_thought(
                    "orchestrator", 
                    "task_completed", 
                    {"task_id": task.task_id, "status": task.status, "self_evaluation": task.self_evaluation}
                )
                
                if not success: break
            
            if any(t.status == "failed" for t in completed_tasks.values()):
                self.workspace.add_thought("orchestrator", "execution_halted", "A task failed, halting plan execution.")
                break
        
        reporter_tasks = [t for t in plan.tasks if t.expert_name.lower() == 'reporter']
        if reporter_tasks:
             self.workspace.add_thought("orchestrator", "reporting_start", "Phase 3: Reporting")
             final_report = self.reporter_agent.execute(plan, experts)
             self.workspace.set_final_answer(final_report)
             return final_report
        else:
            if not completed_tasks: return "タスクは実行されましたが、結果がありませんでした。"
            succeeded_tasks = [t for t in completed_tasks.values() if t.status == "completed"]
            if succeeded_tasks:
                last_task = max(succeeded_tasks, key=lambda t: t.task_id)
                final_result = last_task.result or "完了しましたが結果がありません。"
                self.workspace.set_final_answer(final_result)
                return final_result
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

    def _build_context_for_task(self, task: SubTask, plan: Plan, completed_tasks: Dict[int, SubTask], rag_results: List[Document], tool_results: str = "") -> Dict[str, Any]:
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
            "rag_results": [doc.content for doc in rag_results],
            "tool_results": tool_results
        }

    def _build_minimal_context(self, prompt: str) -> Dict[str, Any]:
        return {
            "original_prompt": prompt,
            "overall_goal": prompt,
            "milestone": Milestone(milestone_id=1, title="Direct Task", description=prompt),
            "dependency_results": "",
            "rag_results": []
        }

