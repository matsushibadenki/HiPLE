# **HiPLE (Hierarchical Predictive Language Engine): 階層型思考AIシステム**

## **1\. 設計思想：思考の階層化と協調による文脈理解**

このシステムは、単一の巨大モデルが全てのタスクを処理するのではなく、人間の思考プロセスを模倣した\*\*「思考の階層化」**と**「専門家による協調」\*\*をアーキテクチャレベルで実現することを目的としています。

複雑な問題に対し、まず\*\*階層的な計画（抽象思考）**を行い、その計画の全体像と各ステップの目的を理解します。そして、タスク実行時には、必要に応じて他の専門家（エキスパートAI）に**助言を求める（協調的推論）\*\*ことで、長期的で一貫性のある文脈を維持しつつ、多角的な視点を取り入れた質の高い成果を生み出します。

### **思考の3階層モデル**

* **L1: 全体目標 (Overall Goal)**  
  * ユーザーからの曖昧な要求を受け取り、タスクの核心を見抜き、最終的なゴールを定義します。  
* **L2: 主要マイルストーン (Key Milestones)**  
  * 最終ゴールに至るまでの中間目標を設定します。物語における「章」のように、論理的な区切りとして機能します。  
* **L3: 具体的なサブタスク (Actionable Subtasks)**  
  * 各マイルストーンを達成するための、専門家（エキスパートAI）が実行可能な個別のタスクです。このタスクには、必要に応じて\*\*「相談相手」\*\*が指定されます。

このアーキテクチャにより、AIは「自分が今、大きな流れのどこにいるのか」を常に把握しながら、個々の専門性を最大限に活かしつつ、他のAIと協力して作業を進めることができ、スケーラビリティ、柔軟性、そしてAIの思考プロセスの透明性を実現します。

## **2\. システムアーキテクチャ**

```mermaid
graph TD  
    A\[User Prompt\] \--\> P\[HiPLE-P Planner Agent\]  
      
    P \-- "Hierarchical Plan (with consultation steps)" \--\> O\[HipleOrchestrator\]  
      
    subgraph HiPLE\_Core\[HiPLE Core\]  
        O \-- "Context \+ Task" \--\> G\[HiPLE-G Generator Agent\]  
          
        subgraph Expert\_Pool\[Available Experts\]  
            direction LR  
            E1\[Jamba\]  
            E2\[HRM Reasoner\]  
            E3\[Transformer Coder\]  
            E4\[Visualizer\]  
        end

        G \-- "1. Needs Consultation?" \--\> C\[Consultant Agent\]  
        C \-- "2. Gathers Advice" \--\> Expert\_Pool  
        Expert\_Pool \-- "3. Provides Advice" \--\> C  
        C \-- "4. Summarizes Advice" \--\> G  
        G \-- "5. Executes Task with Advice" \--\> Expert\_Pool  
          
        G \-- "Final Task Result" \--\> O  
        O \-- "Integrated Results" \--\> R\[Reporter Agent\]  
    end  
      
    R \-- Final Response \--\> F\[Final Response\]
```

## **3\. ディレクトリ構成**

/hybrid\_llm\_system  
├── agents/  
│   ├── base\_agent.py  
│   ├── planner\_agent.py      \# HiPLE-P: 計画立案  
│   ├── generator\_agent.py    \# HiPLE-G: タスク実行  
│   ├── consultant\_agent.py   \# HiPLE-C: 専門家への相談  
│   └── reporter\_agent.py     \# 結果統合  
├── config/  
│   └── models.yml            \# モデル設定  
├── container/  
│   └── container.py          \# DIコンテナ  
├── domain/  
│   ├── schemas.py            \# データスキーマ  
│   └── model\_manager.py      \# モデル管理  
├── model\_files/              \# .ggufファイル配置  
├── orchestrator/  
│   └── hiple\_orchestrator.py \# メイン制御  
├── services/  
│   ├── model\_loader.py       \# モデルローダー  
│   ├── worker\_manager.py     \# 外部プロセス管理  
│   ├── plan\_evaluation\_service.py \# 計画評価  
│   └── retrieval\_service.py  \# RAGサービス  
├── .env                      \# 環境変数  
├── main.py                   \# エントリーポイント  
└── requirements.txt          \# 依存関係

## **4\. セットアップとインストール**

### **ステップ1: 依存ライブラリのインストール**

pip install \-r requirements.txt

### **ステップ2: LLMモデルのダウンロード**

model\_files ディレクトリを作成し、以下のGGUF形式のモデルファイルを配置してください：

| モデル | 用途 | ダウンロード先 |
| :---- | :---- | :---- |
| **Jamba** | 高速推論 | [mradermacher/AI21-Jamba-Mini-1.7-i1-GGUF](https://huggingface.co/mradermacher/AI21-Jamba-Mini-1.7-i1-GGUF) |
| **Gemma** | 汎用処理 | [google/gemma-3-4b-it-qat-q4\_0-gguf](https://huggingface.co/google/gemma-3-4b-it-qat-q4_0-gguf) |
| **HRM** | 深層推論 | [DavidAU/L3.1-Dark-Reasoning-Dark-Planet-Hermes-R1-Uncensored-Horror-Imatrix-MAX-8B-GGUF](https://huggingface.co/DavidAU/L3.1-Dark-Reasoning-Dark-Planet-Hermes-R1-Uncensored-Horror-Imatrix-MAX-8B-GGUF) |
| **Stable Diffusion** | 画像生成 | [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) |

### **ステップ3: 環境変数の設定**

.env.sample を参考に .env ファイルを作成し、各モデルへのパスを設定してください：

\# .env ファイル例  
JAMBA\_MODEL\_PATH="./model\_files/AI21-Jamba-Mini-1.7.i1-IQ1\_S.gguf"  
TRANSFORMER\_MODEL\_PATH="./model\_files/gemma-3-4b-it-q4\_0.gguf"  
HRM\_MODEL\_PATH="./model\_files/L3.1-Dark-Reason-Dark-Plnt-Hrm-R1-Uncen-Hrr-Imtr-MAX-8B-D\_AU-IQ3\_XXS-imat.gguf"  
LIQUIDS4\_MODEL\_PATH=""  
VISUALIZER\_MODEL\_ID="stabilityai/stable-diffusion-xl-base-1.0"

## **5\. 使い方**

### **基本的な起動**

python main.py

### **対話的な使用例**

\# システム起動後  
\> Pythonで簡単なWebサーバーを実装し、そのアーキテクチャを説明する画像も生成してください。

\# HiPLE-P が計画を立案（コーディングと画像生成のタスク、相互に相談）  
\# HiPLE-G と HiPLE-C が連携してタスクを実行  
\# 最終的な統合レポート（コードと画像パス）を出力

## **6\. 動作の仕組み**

1. **初期化**: main.py がDIコンテナを通じて HipleOrchestrator と各エージェントを初期化します。  
2. **計画立案 (HiPLE-P)**: ユーザーからプロンプトを受け取ると、オーケストレーターは **PlannerAgent** を呼び出します。PlannerAgentは、ユーザーの要求を分析し、達成に必要なサブタスクのリスト（実行計画）を動的に生成します。この際、複雑なタスクには、助言を求めるべき他のエキスパート（consultation\_experts）を指定します。  
3. **計画検証**: オーケストレーターは、生成された計画が構造的・意味的に妥当であるかを **PlanEvaluationService** を用いて検証します。問題があれば、エラー内容をPlannerAgentにフィードバックし、計画を修正させます（自己修正ループ）。  
4. **協調的実行 (HiPLE-G & C)**: 検証済みの計画に従い、オーケストレーターはタスクを一つずつ **GeneratorAgent** に渡します。  
   * **相談**: GeneratorAgentは、タスクに相談相手が指定されている場合、まず **ConsultantAgent** を呼び出します。  
   * **助言収集**: ConsultantAgentは、指定された相談相手のエキスパートたちに助言を求め、その結果を要約してGeneratorAgentに返します。  
   * **実行**: GeneratorAgentは、受け取った助言を元のタスクのコンテキストに加えてプロンプトを構築し、主担当のエキスパートにタスクを実行させます。  
5. **結果統合 (Reporter)**: 全てのタスクが完了すると、オーケストレーターは **ReporterAgent** を呼び出します。ReporterAgentは、全ての成果を統合し、ユーザーの元の要求に対する最終的な回答を生成して返します。

## **7\. 特徴**

* **透明性**: 各ステップの思考プロセス（計画、相談、実行）が可視化されます。  
* **協調性**: エキスパートが互いに助言しあうことで、単一モデルでは到達できない高品質な結果を生成します。  
* **自己修正**: 計画の論理的な矛盾を自ら発見し、修正する能力を持ちます。  
* **効率性**: タスクに応じて最適なモデルを選択し、リソースを効率的に利用します。  
* **スケーラビリティ**: モジュラー設計により、新しいエキスパートや機能の拡張が容易です。

## **8\. RoadMap**

* **長期記憶**: 計画ベクトルをデータベースに保存し、過去の経験から学ぶ自己成長型AIへ。  
* **思考の可視化**: AIの計画プロセスをUIで可視化し、人間がAIの思考
