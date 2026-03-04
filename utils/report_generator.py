def generate_report(market, business, competition, risk, score):

    report = f"""
# Startup Evaluation Report

## Executive Summary
AI analysis of the startup pitch.

---

## Market Opportunity
{market}

---

## Business Model
{business}

---

## Competitive Advantage
{competition}

---

## Funding Risk
{risk}

---

## Investor Readiness Score
**{score} / 100**

---

## Recommendations

• Improve TAM/SAM justification

• Add stronger competitive moat

• Show revenue traction

• Include clearer pricing details

• Provide customer traction metrics
"""

    return report