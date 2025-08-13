# **HiPLE (Hierarchical Predictive Language Engine)**

**階層型思考AIシステム**

## **1\. 設計思想**

### **思考の階層化と協調による文脈理解**

このシステムは単一の巨大モデルが全てを処理するのではなく、人間の思考プロセスを模倣した\*\*「思考の階層化」**と**「専門家による協調」\*\*をアーキテクチャレベルで実現します。

複雑な問題に対し、まず\*\*階層的な計画（抽象思考）**を行い、計画の全体像と各ステップの目的を理解します。タスク実行時には、必要に応じて他の専門家（エキスパートAI）に**助言を求める（協調的推論）\*\*ことで、長期的で一貫性のある文脈を維持しつつ、多角的な視点を取り入れた質の高い成果を生み出します。

### **思考の3階層モデル**

| 階層 | 名称 | 役割 |
| :---- | :---- | :---- |
| **L1** | **全体目標 (Overall Goal)** | ユーザーの曖昧な要求を受け取り、タスクの核心を見抜き、最終的なゴールを定義 |
| **L2** | **主要マイルストーン (Key Milestones)** | 最終ゴールに至るまでの中間目標を設定。物語の「章」のように論理的な区切りとして機能 |
| **L3** | **具体的なサブタスク (Actionable Subtasks)** | 各マイルストーンを達成するための、専門家が実行可能な個別タスク。必要に応じて「相談相手」を指定 |

このアーキテクチャにより、AIは「自分が今、大きな流れのどこにいるのか」を常に把握し、個々の専門性を最大限に活かしながら他のAIと協力して作業を進めることで、スケーラビリティ、柔軟性、思考プロセスの透明性を実現します。

## **2\. システムアーキテクチャ**

```mermaid
graph TD  
    subgraph UserInteraction  
        A\["User Prompt"\]  
    end

    subgraph HiPLE\_Orchestration  
        O\["HipleOrchestrator"\]  
        P\["PlannerAgent"\]  
        R\["ReporterAgent"\]  
        TR\["ToolRouterAgent"\]  
    end

    subgraph Services  
        PTS\["PerformanceTrackerService"\]  
        MM\["ModelManager"\]  
        PES\["PlanEvaluationService"\]  
        RAGM\["RAGManagerService"\]  
    end

    subgraph Agents\_And\_Tools  
        G\["GeneratorAgent"\]  
        C\["ConsultantAgent"\]  
        RAGA\["RAGAgent"\]  
        subgraph Expert\_Pool\["Available Experts"\]  
            direction LR  
            E1\["Jamba"\]  
            E2\["HRM Reasoner"\]  
            E3\["Transformer Coder"\]  
        end  
        subgraph External\_Tools  
            W\["WikipediaAgent"\]  
        end  
    end  
      
    subgraph RAG\_Core  
        DS\["DataSources (Plan, File, etc.)"\]  
        RT\["Retrievers (Faiss, BM25, etc.)"\]  
    end

    A \--\> O  
    O \-- "Route Task" \--\> TR  
    TR \-- "Decision" \--\> O

    O \-- "Needs Plan" \--\> P  
    P \-- "Consults" \--\> PTS  
    P \-- "Hierarchical Plan" \--\> O  
    O \-- "Validates Plan" \--\> PES  
      
    O \-- "Execute Plan" \--\> RAGM  
    RAGM \-- "Build Index" \--\> RT  
    RT \-- "Uses" \--\> DS

    O \-- "Execute Task" \--\> G  
    G \-- "Needs Context?" \--\> RAGA  
    RAGA \-- "Retrieval Decision" \--\> O  
    O \-- "Query" \--\> RAGM  
    RAGM \-- "Retrieve" \--\> RT  
    RT \-- "Relevant Docs" \--\> O  
    O \-- "Context" \--\> G  
      
    G \-- "Needs Consultation?" \--\> C  
    C \-- "Gathers Advice" \--\> Expert\_Pool  
      
    G \-- "Executes Task" \--\> Expert\_Pool  
    G \-- "Task Result" \--\> O  
    O \-- "Updates" \--\> PTS

    O \-- "Needs Final Report" \--\> R  
    R \-- "Integrated Results" \--\> O

    O \-- "Tool-Use" \--\> External\_Tools

    O \-- "Final Response" \--\> A
```

## **3\. ディレクトリ構成**

/HiPLE
├── agents/  
│   ├── base\_agent.py  
│   ├── planner\_agent.py  
│   ├── generator\_agent.py  
│   ├── consultant\_agent.py  
│   ├── reporter\_agent.py  
│   ├── tool\_router\_agent.py  
│   └── rag\_agent.py            \# (新規) RAG判断エージェント  
├── config/  
│   └── models.yml  
├── container/  
│   └── container.py  
├── domain/  
│   ├── schemas.py  
│   └── evaluation.py  
│   └── model\_manager.py  
├── model\_files/  
├── orchestrator/  
│   └── hiple\_orchestrator.py  
├── rag/                        \# (新規) Modular RAGコア  
│   ├── \_\_init\_\_.py  
│   ├── data\_sources.py  
│   └── retrievers.py  
├── services/  
│   ├── model\_loader.py  
│   ├── worker\_manager.py  
│   ├── plan\_evaluation\_service.py  
│   ├── performance\_tracker\_service.py  
│   └── rag\_manager\_service.py    \# (新規) RAG管理サービス  
├── .env  
├── main.py  
└── requirements.txt

## **4\. セットアップとインストール**

### **ステップ1: 依存ライブラリのインストール**

pip install \-r requirements.txt

### **ステップ2: LLMモデルのダウンロード**

model\_files ディレクトリを作成し、GGUF形式のモデルファイルを配置してください。

### **ステップ3: 環境変数の設定**

.env.sample を参考に .env ファイルを作成し、各モデルへのパスを設定してください。

## **5\. 使い方**

### **基本的な起動**

python main.py

### **パフォーマンスの確認**

セッション中のエキスパートのパフォーマンスを確認するには、以下のコマンドを入力します。

\> show performance

## **6\. 動作の仕組み**

### **処理フロー**

1. **初期化**: main.py がDIコンテナを通じて HipleOrchestrator と各サービス・エージェントを初期化。  
2. **要求分析 (ToolRouterAgent)**: ユーザープロンプトを分析し、タスクの種類（単純応答、複雑な計画、ツール利用）を判断。  
3. **計画立案 (PlannerAgent)**: 複雑なタスクの場合、PerformanceTrackerServiceから得られる実績を考慮し、最適な担当者を割り当てた階層的計画を生成。  
4. **RAGインデックス構築 (RAGManagerService)**: 生成された計画全体を一つの知識ベースとして、RAGManagerServiceが検索インデックスを構築。  
5. **協調的実行 (GeneratorAgent & Co.)**:  
   * **RAG判断 (RAGAgent)**: 各タスクを実行する前に、RAGAgentが計画内の文脈検索が必要かを判断。  
   * **検索 (RAGManagerService)**: 検索が必要な場合、RAGManagerServiceがインデックスから関連情報を取得。  
   * **相談 (ConsultantAgent)**: 必要に応じて他の専門家から助言を収集。  
   * **実行 (GeneratorAgent)**: 検索結果や助言を含む全てのコンテキストを基に、主担当エキスパートがタスクを実行。  
6. **パフォーマンス記録**: 各タスクの実行後、結果（成功/失敗、実行時間）を PerformanceTrackerService に記録。  
7. **結果統合 (ReporterAgent)**: 全てのタスク完了後、ReporterAgentが成果を統合し、最終的な回答を生成。

## **7\. 特徴**

### **🧩 Modular RAG**

データソース、検索アルゴリズム、テキスト分割方法などを独立したモジュールとして扱えるため、高い拡張性と柔軟性を持ちます。

### **🧠 動的エキスパート選択**

タスクごとに過去の成功率や処理速度に基づき、最も適したAIを自動で選択。経験から学びます。

### **🔍 透明性**

各ステップの思考プロセスが可視化されます。show performanceコマンドで、各AIの現在の評価を確認できます。

### **🤝 協調性**

エキスパートが互いに助言しあうことで、単一モデルでは到達できない高品質な結果を生成します。

### **🔄 自己修正**

計画の論理的な矛盾を自ら発見し、修正する能力を持ちます。

## **8\. ロードマップ**

### **🧠 長期記憶**

計画ベクトルやパフォーマンス記録を永続化DBに保存し、過去の経験から学ぶ自己成長型AIへ。

### **📊 思考の可視化**

AIの計画プロセスをUIで可視化し、人間がAIの思考過程を理解できるインターフェースを提供。

### **🔧 機能拡張**

* ファイルやWebページをRAGのデータソースとして追加。  
* より多様な専門家エージェントの追加。  
* 外部ツールとの連携強化。
