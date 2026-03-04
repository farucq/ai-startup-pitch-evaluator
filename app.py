import streamlit as st

from ingestion.pdf_parser import parse_pdf
from embeddings.embedder import load_embeddings
from vectorstore.vectordb import create_vectorstore
from rag.retriever import get_retriever

from llm.llm_provider import get_llm

from analyzers.market_analyzer import analyze_market
from analyzers.business_model import analyze_business
from analyzers.competition import analyze_competition
from analyzers.risk_assessment import assess_risk

from scoring.scoring_engine import calculate_score
from utils.report_generator import generate_report

st.title("AI Startup Pitch Evaluator")

uploaded_file = st.file_uploader(
    "Upload Pitch Deck",
    type=["pdf"]
)

if uploaded_file:

    st.write("Processing pitch deck...")

    docs = parse_pdf(uploaded_file)

    embeddings = load_embeddings()

    vectordb = create_vectorstore(docs, embeddings)

    retriever = get_retriever(vectordb)

    llm = get_llm()

    market = analyze_market(llm, retriever)
    business = analyze_business(llm, retriever)
    competition = analyze_competition(llm, retriever)
    risk = assess_risk(llm, retriever)

    score = calculate_score(
        market,
        business,
        competition,
        risk
    )

    report = generate_report(
        market,
        business,
        competition,
        risk,
        score
    )


    st.write(report)