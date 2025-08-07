# path: ./orchestrator/hiple_orchestrator.py
# title: Main Orchestrator using HRM for Simple Tasks
# description: 単純なタスクの処理を、不安定なJambaから安定したHRMに切り替える司令塔。

import traceback
from typing import Dict, List, Tuple, Any
from domain.model_manager import ModelManager
from domain.schemas import SubTask, Plan, ExpertModel, Milestone
from agents.planner_agent import PlannerAgent
from agents.generator_agent import GeneratorAgent
from agents.reporter_agent import ReporterAgent
from agents.router_agent import RouterAgent
from services.retrieval_service import RetrievalService

class HipleOrchestrator:
    """
    HiPLEアーキテクチャに基づき、思考プロセス全体を管理する。
    RouterAgentを使い、タスクの複雑に応じて処理を振り分ける。
    """
    def __init__(
        self,
        model_manager: ModelManager,
        planner_agent: PlannerAgent,
        generator_agent: GeneratorAgent,
        reporter_agent: ReporterAgent,
        router_agent: RouterAgent,
        retrieval_service: RetrievalService,
    ):
        self.model_manager = model_manager
        self.planner_agent = planner_agent
        self.generator_agent = generator_agent
        self.reporter_agent = reporter_agent
        self.router_agent = router_agent
        self.retrieval_service = retrieval_service

    def process_task(self, prompt: str) -> str:
        """
        タスク処理のメインエントリーポイント。
        まず要求の複雑さを判断し、適切な処理フローに分岐させる。
        """
        print(f"▶️ HiPLEタスク開始: {prompt}")
        try:
            active_experts = self.model_manager.get_all_experts()
            if not active_experts: return "エラー: 利用可能なエキスパートがいません。"

            print("\n--- Phase 0: Routing ---")
            task_type = self.router_agent.execute(prompt, active_experts)
            print(f"🧠 ルーティング結果: {task_type.upper()}")

            if task_type == "simple":
                return self._process_simple_task(prompt, active_experts)
            else: # complex
                return self._process_complex_task(prompt, active_experts)

        except Exception as e:
            traceback.print_exc()
            return f"致命的なエラーが発生しました: {e}"

    def _process_simple_task(self, prompt: str, experts: List[ExpertModel]) -> str:
        """
        単純なタスクを直接実行する。
        """
        print("\n--- Direct Generation (using HRM for stability) ---")
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↓修正開始◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        # 不安定なJambaの代わりに、安定しているHRMを対話に使用する
        expert = self.model_manager.get_expert("HRM")
        if not expert:
            return "エラー: 単純応答用のエキスパート'HRM'が見つかりません。"
        
        # HRMに対話的な応答を促すためのシンプルなシステムプロンプト
        expert.system_prompt = "あなたは、ユーザーの質問に誠実かつ簡潔に答える、優秀なAIアシスタントです。"
        # ◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️↑修正終わり◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
        
        task = SubTask(task_id=1, description=prompt, expert_name=expert.name)
        context = self._build_minimal_context(prompt)
        
        return self.generator_agent.execute(task, expert, context)

    def _process_complex_task(self, prompt: str, experts: List[ExpertModel]) -> str:
        """
        複雑なタスクに対して、階層的な計画を立てて実行する。
        """
        print("\n--- Phase 1: Hierarchical Planning (HiPLE-P) ---")
        current_plan = self.planner_agent.execute(prompt, experts)
        
        print(f"L1 (Goal): {current_plan.overall_goal}")
        for m in current_plan.milestones:
            print(f"L2 (Milestone {m.milestone_id}): {m.title}")
        
        is_valid, error_msg = self._validate_plan(current_plan, experts)
        if not is_valid:
            print(f"⚠️ 計画の検証に失敗: {error_msg}。フォールバック処理に移行します。")
            return self._process_simple_task(prompt, experts)

        self.retrieval_service.build_index(current_plan)

        print("\n--- Phase 2: Context-Aware Generation (HiPLE-G) ---")
        completed_tasks: Dict[int, SubTask] = {}
        
        worker_tasks = [t for t in current_plan.tasks if t.expert_name.lower() != 'reporter']
        
        while len(completed_tasks) < len(worker_tasks):
            executable_tasks = [t for t in worker_tasks if t.status == "pending" and all(d in completed_tasks for d in t.dependencies)]
            
            if not executable_tasks:
                if len(completed_tasks) < len(worker_tasks):
                    return "エラー: タスクの依存関係が循環しているか、計画に問題があります。"
                break

            for task in executable_tasks:
                expert = self.model_manager.get_expert(task.expert_name)
                if not expert:
                    print(f"⚠️ タスク {task.task_id} のエキスパート '{task.expert_name}' が見つかりません。スキップします。")
                    task.result = f"エラー: エキスパート '{task.expert_name}' が見つかりませんでした。"
                    task.status = "failed"
                    completed_tasks[task.task_id] = task
                    continue
                
                context = self._build_context_for_task(task, current_plan, completed_tasks)
                
                print(f"\n▶️ Executing Task {task.task_id} ({task.expert_name.upper()}): {task.description}")
                task.status = "in_progress"
                task.result = self.generator_agent.execute(task, expert, context)
                task.status = "completed"
                completed_tasks[task.task_id] = task
                print(f"✅ Task {task.task_id} Completed.")

        reporter_tasks = [t for t in current_plan.tasks if t.expert_name.lower() == 'reporter']
        if reporter_tasks:
             print("\n--- Phase 3: Reporting ---")
             final_report = self.reporter_agent.execute(current_plan, experts)
             print("✅ 全てのタスクが正常に完了しました。")
             return final_report
        else:
            print("\n✅ 全てのタスクが正常に完了しました。")
            if not completed_tasks: return "タスクは実行されましたが、結果がありませんでした。"
            last_task = max(completed_tasks.values(), key=lambda t: t.task_id)
            return last_task.result or "完了しましたが結果がありません。"

    def _validate_plan(self, plan: Plan, experts: List[ExpertModel]) -> Tuple[bool, str]:
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

    def _build_context_for_task(self, task: SubTask, plan: Plan, completed_tasks: Dict[int, SubTask]) -> Dict[str, Any]:
        current_milestone = next((m for m in plan.milestones if m.milestone_id == task.milestone_id), None)
        dependency_results = ""
        if task.dependencies:
            for dep_id in sorted(task.dependencies):
                if dep_id in completed_tasks:
                    result = completed_tasks[dep_id].result
                    dependency_results += f"【先行タスク{dep_id}の結果】:\n{result}\n\n"
        rag_results = self.retrieval_service.search(task.description, k=3)
        return {
            "original_prompt": plan.original_prompt,
            "overall_goal": plan.overall_goal,
            "milestone": current_milestone,
            "dependency_results": dependency_results,
            "rag_results": rag_results
        }
    
    def _build_minimal_context(self, prompt: str) -> Dict[str, Any]:
        """単純なタスク用の最小限のコンテキストを構築する"""
        return {
            "original_prompt": prompt,
            "overall_goal": prompt,
            "milestone": Milestone(milestone_id=1, title="Direct Task", description=prompt),
            "dependency_results": "",
            "rag_results": []
        }