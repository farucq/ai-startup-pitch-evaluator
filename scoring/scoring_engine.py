import re


def calculate_score(market, business, competition, risk):

    score = 0

    # Market score
    if "TAM" in market or "market" in market.lower():
        score += 20
    else:
        score += 10

    # Business model score
    if "revenue" in business.lower():
        score += 20
    else:
        score += 10

    # Competition score
    if "competitor" in competition.lower():
        score += 15
    else:
        score += 8

    # Risk score extraction
    risk_score = 10

    match = re.search(r'(\d+)', risk)

    if match:
        risk_score = int(match.group(1)) // 5

    score += risk_score

    # Innovation score
    if "AI" in market or "AI" in competition:
        score += 15
    else:
        score += 10

    return min(score, 100)