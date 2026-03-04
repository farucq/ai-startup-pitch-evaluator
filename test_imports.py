#!/usr/bin/env python3

print("Testing imports...")

try:
    import streamlit as st
    print("✓ streamlit imported")
except ImportError as e:
    print(f"✗ streamlit: {e}")

try:
    from ingestion.pdf_parser import parse_pdf
    print("✓ pdf_parser imported")
except ImportError as e:
    print(f"✗ pdf_parser: {e}")

try:
    from embeddings.embedder import load_embeddings
    print("✓ embedder imported")
except ImportError as e:
    print(f"✗ embedder: {e}")

try:
    from vectorstore.vectordb import create_vectorstore
    print("✓ vectordb imported")
except ImportError as e:
    print(f"✗ vectordb: {e}")

try:
    from rag.retriever import get_retriever
    print("✓ retriever imported")
except ImportError as e:
    print(f"✗ retriever: {e}")

try:
    from llm.llm_provider import get_llm
    print("✓ llm_provider imported")
except ImportError as e:
    print(f"✗ llm_provider: {e}")

try:
    from analyzers.market_analyzer import analyze_market
    print("✓ market_analyzer imported")
except ImportError as e:
    print(f"✗ market_analyzer: {e}")

try:
    from analyzers.business_model import analyze_business
    print("✓ business_model imported")
except ImportError as e:
    print(f"✗ business_model: {e}")

try:
    from analyzers.competition import analyze_competition
    print("✓ competition imported")
except ImportError as e:
    print(f"✗ competition: {e}")

try:
    from analyzers.risk_assessment import assess_risk
    print("✓ risk_assessment imported")
except ImportError as e:
    print(f"✗ risk_assessment: {e}")

try:
    from scoring.scoring_engine import calculate_score
    print("✓ scoring_engine imported")
except ImportError as e:
    print(f"✗ scoring_engine: {e}")

try:
    from utils.report_generator import generate_report
    print("✓ report_generator imported")
except ImportError as e:
    print(f"✗ report_generator: {e}")

print("\nAll imports tested!")
