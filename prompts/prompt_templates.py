market_prompt = """
Analyze the startup pitch and evaluate market opportunity.

Context:
{context}

Return:
- TAM/SAM/SOM evaluation
- Market growth potential
- Scalability signals
"""

business_prompt = """
Evaluate the business model.

Context:
{context}

Return:
- Revenue streams
- Pricing model
- Customer acquisition strategy
- Missing details
"""

competition_prompt = """
Analyze competitive advantage.

Context:
{context}

Return:
- Competitors mentioned
- Differentiation
- Weak positioning
"""

risk_prompt = """
Identify funding risks.

Context:
{context}

Return:
- Execution risk
- Market risk
- Financial risk
- Risk score (0-100)
"""