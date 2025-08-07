# **HiPLE Project Roadmap**

## **1\. プロジェクトビジョン**

HiPLE (Hierarchical Predictive Language Engine) は、単一の巨大モデルに依存するのではなく、人間の思考プロセスを模倣した\*\*「思考の階層化」\*\*をアーキテクチャレベルで実現することを目指しています。

このロードマップは、HiPLEが単純なタスク処理システムから、自律的に学習・成長し、複雑な問題解決を人間と協調しながら行う\*\*「自己成長型AIパートナー」\*\*へと進化するための道筋を示すものです。

## **2\. ロードマップ全体像**

```
gantt  
    title HiPLE Development Roadmap  
    dateFormat  YYYY-MM-DD  
    axisFormat  %Y-%m  
      
    section Phase 1: 基盤強化と対話的進化  
    長期記憶の実現 (Persistent Memory)        :active, p1\_1, 2025-08-08, 2m  
    思考の可視化と介入 (Visualization & Intervention) :p1\_2, after p1\_1, 3m  
    対話型・動的プランナー (Interactive Planner)    :p1\_3, after p1\_1, 3m  
    グローバル・ワークスペース実装 (Global Workspace)  :p1\_4, after p1\_2, 2m

    section Phase 2: 自律性と能力拡張  
    ツール利用能力の獲得 (Tool-Use)          :p2\_1, after p1\_4, 4m  
    高度なワークフロー制御 (Advanced Workflow) :p2\_2, after p2\_1, 3m  
    失敗からの学習 (Learning from Failure)     :p2\_3, after p2\_2, 3m

    section Phase 3: 自己進化するエコシステム  
    動的エキスパート評価・選択 (Dynamic Expert Selection) :p3\_1, after p2\_3, 4m  
    自己成長型プランニング (Self-Improving Planner)    :p3\_2, after p3\_1, 6m  
    エコシステムの拡張 (Ecosystem Expansion)         :p3\_3, after p3\_2, 6m
```

## **Phase 1: 基盤強化と対話的進化 (Core Functionality & Interactive Evolution)**

**目標:** システムの記憶力と透明性を向上させ、人間がAIの思考プロセスに自然に介入できる対話型システムを確立する。

### **1-1. 長期記憶の実現 (Persistent Memory)**

* **引用元:** README.md \> 8\. RoadMap \> ・**長期記憶**  
* **What:** 現在は実行ごとに破棄される計画や結果のベクトル情報を、FAISSやChromaDBのような永続化可能なベクトルデータベースに保存します。  
* **Why:** 過去の実行経験（成功・失敗）を資産として蓄積し、類似タスクの解決に応用することで、AIが経験から学ぶことを可能にします。  
* **How:**  
  1. RetrievalServiceを改修し、永続化DB（例: ChromaDB）と接続します。  
  2. HipleOrchestratorがタスクを完了するたびに、計画(Plan)と各SubTaskの結果をベクトル化してDBに保存する処理を追加します。  
  3. PlannerAgentが新しい計画を立てる際に、過去の類似計画をDBから検索し、参考情報としてプロンプトに含めるようにします。

### **1-2. 思考の可視化と介入 (Visualization & Intervention)**

* **引用元:** README.md \> 8\. RoadMap \> ・**思考の可視化**  
* **What:** 現在のCUIベースの対話に加え、FlaskやFastAPIを用いたWeb UIを開発します。UI上では、生成された計画の階層構造（L1-L3）や各タスクの実行状況がリアルタイムで表示されます。  
* **Why:** AIの「考えていること」を人間が直感的に理解できるようにし、システムの透明性と信頼性を向上させます。また、人間がAIの思考プロセスに介入する基盤を築きます。  
* **How:**  
  1. main.pyから呼び出されるWebサーバーアプリケーションを構築します。  
  2. HipleOrchestratorの実行状態をWebSocketなどを通じてフロントエンドに送信します。  
  3. フロントエンドでは、Mermaid.jsやD3.jsなどを用いて、計画の進捗を動的に可視化します。  
  4. UI上に「一時停止」「再開」「タスク編集」ボタンを設け、HipleOrchestratorに指示を送るAPIを実装します。

### **1-3. 対話型・動的プランナー (Interactive & Dynamic Planner)**

* **引用元:** README.md \> 8\. RoadMap \> ・**動的プランナー**  
* **What:** PlannerAgentが生成した計画を一度ユーザーに提示し、承認や修正を求める対話ループを導入します。  
* **Why:** AIの自動計画に人間の意図を反映させることで、より精度の高い、ユーザーの要求に沿ったタスク実行を実現します。  
* **How:**  
  1. HipleOrchestratorの\_process\_complex\_taskに、計画生成後、ユーザーに確認を求めるステップを追加します。  
  2. ユーザーからのフィードバック（例：「ステップ2は不要」「ステップ3の前にコーディングを追加して」）を解析し、PlannerAgentに再計画を指示するプロンプトを生成します。

### **1-4. グローバル・ワークスペースの実装 (Global Workspace)**

* **What:** workspace/global\_workspace.pyの設計思想を全面的に採用し、DIコンテナを通じてシングルトンインスタンスとして全エージェントに共有します。  
* **Why:** エキスパート間の情報共有を確実かつ効率的に行い、システム全体の文脈理解度を向上させます。デバッグも容易になります。  
* **How:**  
  1. container.pyにGlobalWorkspaceをシングルトンとして登録します。  
  2. HipleOrchestratorおよび全エージェントのコンストラクタを修正し、GlobalWorkspaceをDIします。  
  3. 各エージェントは、自身の処理結果や中間生成物をGlobalWorkspaceに書き込むように処理を統一します。

## **Phase 2: 自律性と能力拡張 (Autonomy & Capability Expansion)**

**目標:** 外部世界との連携を可能にし、より複雑なワークフローを自律的に処理できる能力を獲得する。

### **2-1. ツール利用能力の獲得 (Tool-Use Integration)**

* **What:** エキスパートが外部API（Web検索、電卓、コード実行など）を呼び出せるようにします。  
* **Why:** LLM単体の知識や能力の限界を超え、最新情報へのアクセスや正確な計算、安全なコード実行などを可能にします。  
* **How:**  
  1. domain/schemas.pyにツールを定義するスキーマを追加します。  
  2. GeneratorAgentを拡張し、エキスパートからの応答がツール呼び出し形式であった場合に、指定されたツールを実行し、その結果をエキスパートに返す機能を実装します。

### **2-2. 高度なワークフロー制御 (Advanced Workflow Control)**

* **What:** 計画に条件分岐（例：タスクAが成功したらBへ、失敗したらCへ）と、依存関係のないタスクの並列実行を導入します。  
* **Why:** 複雑な問題解決プロセスをより柔軟かつ効率的にモデル化し、実行時間の短縮とロバスト性の向上を実現します。  
* **How:**  
  1. SubTaskスキーマにon\_success, on\_failureなどの条件分岐フィールドを追加します。  
  2. HipleOrchestratorの実行エンジンをasyncioベースに書き換え、依存関係グラフに基づいた非同期・並列実行を可能にします。

### **2-3. 失敗からの学習 (Learning from Failure)**

* **What:** タスクや計画が失敗した際に、その原因（例：APIエラー、コードのバグ、論理的矛盾）をシステムが自ら分析し、計画やプロンプトを自動で修正して再試行する、より高度な自己修正ループを実装します。  
* **Why:** システムの堅牢性を劇的に向上させ、未知のエラーに対しても自律的に回復を試みる自己治癒能力を持たせます。  
* **How:**  
  1. HipleOrchestratorのエラーハンドリングを拡張し、失敗したタスクのコンテキストとエラー情報を分析するFailureAnalysisAgentを導入します。  
  2. 分析結果に基づき、PlannerAgentに具体的な修正指示（例：「このタスクは細分化が必要」「別のアプローチを試せ」）を与えて再計画させます。

## **Phase 3: 自己進化するエコシステム (Self-Evolving Ecosystem)**

**目標:** システムが自らの性能を評価し、改善していく自己進化のサイクルを確立する。また、外部開発者が容易に機能を拡張できるプラグインアーキテクチャを構築する。

### **3-1. 動的エキスパート評価・選択 (Dynamic Expert Selection)**

* **What:** models.ymlの静的な定義に加え、タスクの性質に応じて最適なエキスパート（性能、コスト、速度）をシステムが自律的に評価・選択する仕組みを導入します。  
* **Why:** 常に最適なリソース配分を実現し、システムの運用コストとパフォーマンスを最適化します。  
* **How:**  
  1. 定期的にベンチマークタスクを実行し、各エキスパートの性能を記録するEvaluatorAgentと評価DBを構築します。  
  2. RouterAgentを高度化し、プロンプトの内容と評価DBを照合して、動的に担当エキスパートを決定するようにします。

### **3-2. 自己成長型プランニング (Self-Improving Planner)**

* **What:** 長期記憶に蓄積された大量の成功・失敗計画データをPlannerAgent（HRMモデル）にファインチューニングのデータとして活用し、計画立案能力そのものを継続的に向上させます。  
* **Why:** 人間の手によるプロンプトエンジニアリングを最小限に抑え、AIが自らの経験を通じて「賢くなる」自己成長サイクルを実現します。  
* **How:**  
  1. 蓄積された計画データをLLMのファインチューニングに適した形式に変換するデータパイプラインを構築します。  
  2. 定期的にPlannerAgentのベースモデルを再学習させ、より洗練された計画を生成できるようにします。

### **3-3. エコシステムの拡張 (Ecosystem Expansion)**

* **What:** 外部の開発者が新しい「エキスパート」や「ツール」を簡単に追加できる、明確に定義されたプラグインアーキテクチャ
