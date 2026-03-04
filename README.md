# AI Startup Pitch Evaluator

An AI-powered system that analyzes startup pitch decks and evaluates their investment readiness.
The system extracts key business information from uploaded pitch decks and uses LLM reasoning with Retrieval-Augmented Generation (RAG) to generate structured investment insights, risk assessments, and actionable recommendations for founders and investors.

## Project Objective

The goal of this project is to build an intelligent AI tool that can automatically evaluate startup pitch decks and provide insights similar to those produced by venture capital analysts.

The system performs:

Market opportunity analysis

Business model evaluation

Competitive advantage assessment

Funding risk assessment

Investor readiness scoring

Strategic improvement recommendations

System Architecture

The system follows a Retrieval-Augmented Generation (RAG) architecture.

User Upload Pitch Deck (PDF)
            │
            ▼
     PDF Parsing Module
            │
            ▼
     Text Chunking / Slide Extraction
            │
            ▼
     Embedding Generation
   (Sentence Transformers)
            │
            ▼
       Vector Database
         (ChromaDB)
            │
            ▼
      Semantic Retrieval
            │
            ▼
        LLM Reasoning
         (Groq Llama)
            │
            ▼
     Evaluation Modules
 ├─ Market Opportunity Analyzer
 ├─ Business Model Analyzer
 ├─ Competitive Advantage Evaluator
 └─ Funding Risk Assessment
            │
            ▼
   Investor Readiness Scoring
            │
            ▼
     AI Recommendation Engine
            │
            ▼
     Streamlit Report Output
Workflow
1. Pitch Deck Upload

The user uploads a startup pitch deck (PDF) using the Streamlit interface.

2. Document Ingestion

The system parses the PDF using PyMuPDF, extracting text from each slide.

The document is divided into logical sections for better analysis.

3. Embedding Generation

Each section of the pitch deck is converted into vector embeddings using:

sentence-transformers/all-MiniLM-L6-v2

These embeddings represent semantic meaning.

4. Vector Database Storage

Embeddings are stored in a ChromaDB vector database.

This enables semantic similarity search across pitch deck content.

5. Retrieval-Augmented Generation (RAG)

When the system performs analysis:

Relevant pitch sections are retrieved from the vector database

Retrieved context is provided to the LLM

The LLM generates structured reasoning based on real pitch content

6. AI Analysis Modules

The system includes several AI evaluation modules:

Market Opportunity Analyzer

Evaluates:

TAM / SAM / SOM

Market growth potential

Scalability signals

Business Model Analyzer

Identifies:

Revenue streams

Pricing model

Customer acquisition strategy

Missing business model components

Competitive Advantage Evaluator

Analyzes:

Competitors mentioned in the pitch

Differentiation claims

Strength of market positioning

Funding Risk Assessment Engine

Detects:

Execution risks

Market risks

Financial risks

The module assigns a risk score.

7. Investor Readiness Scoring

The outputs of all evaluation modules are combined using a weighted scoring system to produce a final score:

Investor Readiness Score (0–100)
8. AI Recommendation Generator

The system generates recommendations such as:

Missing slide improvements

Investor-facing presentation tips

Market validation suggestions

Technology Stack
Component	Technology
Backend	Python
LLM	Groq Llama
Framework	LangChain
Embeddings	HuggingFace Sentence Transformers
Vector Database	ChromaDB
PDF Parsing	PyMuPDF
Frontend	Streamlit
Project Structure
ai-startup-pitch-evaluator
│
├── app.py
├── requirements.txt
├── README.md
│
├── analyzers
│   ├── market_analyzer.py
│   ├── business_model.py
│   ├── competition.py
│   └── risk_assessment.py
│
├── embeddings
│   └── embedder.py
│
├── ingestion
│   └── pdf_parser.py
│
├── llm
│   └── llm_provider.py
│
├── prompts
│   └── prompt_templates.py
│
├── rag
│   └── retriever.py
│
├── scoring
│   └── scoring_engine.py
│
├── utils
│   └── report_generator.py
│
└── vectorstore
    └── vectordb.py
Installation
1. Clone the Repository
git clone https://github.com/farucq/ai-startup-pitch-evaluator.git
cd ai-startup-pitch-evaluator
2. Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create .env

GROQ_API_KEY=your_api_key_here
Running the Application

Start the Streamlit app:

streamlit run app.py

Open in browser:

http://localhost:8501

Upload a pitch deck PDF to start the analysis.

Example Output
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
Future Improvements

Possible enhancements include:

Automatic slide classification (Problem, Solution, Market)

Improved scoring models using LLM evaluation

Multi-pitch comparison

Investor dashboard analytics

Pitch deck feedback visualization

License

This project is for educational and research purposes.
