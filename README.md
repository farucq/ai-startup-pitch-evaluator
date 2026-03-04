# AI Startup Pitch Evaluator

An **AI-powered system that analyzes startup pitch decks and evaluates their investment readiness**.

The system extracts key business insights from uploaded pitch decks and uses **Retrieval-Augmented Generation (RAG)** with a Large Language Model (LLM) to generate:

- Market opportunity analysis
- Business model evaluation
- Competitive advantage assessment
- Funding risk assessment
- Investor readiness scoring
- Strategic recommendations for founders

---

# Project Objective

The goal of this project is to build an **AI-driven tool that evaluates startup pitch decks like a venture capital analyst**.

The system automatically analyzes pitch decks and generates structured investor insights including:

- Market opportunity analysis
- Business model evaluation
- Competitive advantage evaluation
- Funding risk assessment
- Investor readiness score
- AI-powered recommendations

---

# System Architecture

The project uses a **Retrieval-Augmented Generation (RAG)** architecture.

```bash
+--------------------------------------------+
|          User Upload Pitch Deck            |
|                  (PDF)                     |
+------------------------------ -------------+
                      |
                      ▼
+--------------------------------------------+
|            PDF Parsing Module              |
|                (PyMuPDF)                   |
+--------------------------------------------+
                      |
                      ▼
+--------------------------------------------+
|        Text Chunking / Slide Split         |
+--------------------------------------------+
                      |
                      ▼
+--------------------------------------------+
|            Embedding Generation            |
|    (Sentence Transformers - MiniLM Model)  |
+--------------------------------------------+
                      |
                      ▼
+--------------------------------------------+
|          Vector Database Storage           |
|               (ChromaDB)                   |
+--------------------------------------------+
                      |
                      ▼
+--------------------------------------------+
|          Semantic Retrieval (RAG)          |
+--------------------------------------------+
                      |
                      ▼
+--------------------------------------------+
|           LLM Reasoning Engine             |
|               (Groq Llama)                 |
+--------------------------------------------+
                      |
                      ▼
+--------------------------------------------+
|              Evaluation Modules            |
|         • Market Opportunity Analyzer      |
|         • Business Model Analyzer          |
|         • Competitive Advantage Evaluator  |
|         • Funding Risk Assessment          |
+--------------------------------------------+
                      |
                      ▼
+--------------------------------------------+
|         Investor Readiness Scoring         |
+--------------------------------------------+
                      |
                      ▼
+--------------------------------------------+
|         AI Recommendation Engine           |
+--------------------------------------------+
                      |
                      ▼
+--------------------------------------------+
|            Streamlit Dashboard UI          |
+--------------------------------------------+
```

---

# Workflow

## 1️.Pitch Deck Upload

The user uploads a **startup pitch deck (PDF)** through the Streamlit interface.

---

## 2️.Document Ingestion

The system parses the PDF using **PyMuPDF**, extracting slide text and preparing it for analysis.

---

## 3️.Text Chunking

The extracted text is segmented into logical sections to improve semantic retrieval.

---

## 4️.Embedding Generation

Each section is converted into vector embeddings using:


sentence-transformers/all-MiniLM-L6-v2


These embeddings represent the semantic meaning of the content.

---

## 5️.Vector Database Storage

Embeddings are stored in **ChromaDB**, which enables semantic similarity search.

---

## 6️.Retrieval-Augmented Generation (RAG)

When analysis is requested:

1. Relevant pitch sections are retrieved from the vector database
2. Retrieved context is passed to the LLM
3. The LLM generates structured analysis

---

## 7️.AI Evaluation Modules

### Market Opportunity Analyzer

Evaluates:

- TAM / SAM / SOM
- Market growth potential
- Scalability signals

---

### Business Model Analyzer

Identifies:

- Revenue streams
- Pricing model
- Customer acquisition strategy
- Missing business components

---

### Competitive Advantage Evaluator

Analyzes:

- Competitors mentioned
- Differentiation strategy
- Market positioning

---

### Funding Risk Assessment Engine

Detects:

- Execution risks
- Market risks
- Financial risks

And generates a **risk score**.

---

## 8️.Investor Readiness Scoring

Outputs from all modules are combined using a **weighted scoring system** to produce:


Investor Readiness Score (0–100)


---

## 9️.AI Recommendation Generator

The system provides improvement suggestions such as:

- Missing slide information
- Investor presentation improvements
- Market validation suggestions

---

# Technology Stack

| Component | Technology |
|--------|--------|
| Programming Language | Python |
| LLM | Groq (Llama models) |
| AI Framework | LangChain |
| Embeddings | HuggingFace Sentence Transformers |
| Vector Database | ChromaDB |
| PDF Parsing | PyMuPDF |
| UI | Streamlit |

---

# Project Structure

```bash
ai-startup-pitch-evaluator
│
├── app.py
├── requirements.txt
├── README.md
│
├── analyzers
│ ├── market_analyzer.py
│ ├── business_model.py
│ ├── competition.py
│ └── risk_assessment.py
│
├── embeddings
│ └── embedder.py
│
├── ingestion
│ └── pdf_parser.py
│
├── llm
│ └── llm_provider.py
│
├── prompts
│ └── prompt_templates.py
│
├── rag
│ └── retriever.py
│
├── scoring
│ └── scoring_engine.py
│
├── utils
│ └── report_generator.py
│
└── vectorstore
└── vectordb.py
```

---

# Installation

## 1️.Clone Repository

```bash
git clone https://github.com/farucq/ai-startup-pitch-evaluator.git
cd ai-startup-pitch-evaluator
```

## 2️.Create Virtual Environment
```bash
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
```
## 3️.Install Dependencies
```bash
pip install -r requirements.txt
```
## 4️.Configure Environment Variables
```bash
Create a .env file:

GROQ_API_KEY=your_api_key_here
```
Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```
Open the browser:
```bash
http://localhost:8501
```
Upload a pitch deck to start the analysis.

### Example Output
```bash
Startup Evaluation Report

Executive Summary
AI analysis of the startup pitch.

Market Opportunity
Logistics market projected to reach $15T by 2025.

Business Model
SaaS subscription model with tiered pricing.

Competitive Advantage
AI-based predictive routing technology.

Funding Risk
Execution risk: Medium
Market risk: Medium
Financial risk: Medium

Investor Readiness Score
78 / 100

Recommendations
• Improve TAM justification
• Show revenue traction
• Strengthen competitive moat
```

---
## Future Improvements

Possible enhancements include:
- Automatic slide classification (Problem / Solution / Market)
- Advanced LLM scoring models
- Multi-pitch comparison
- Investor dashboard analytics
- Pitch feedback visualization


## License

This project is intended for educational and research purposes.

