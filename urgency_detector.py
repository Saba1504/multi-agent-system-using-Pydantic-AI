def detect_urgency(ticket):
    message = ticket["message"].lower()
    urgency_score = 0

    if any(word in message for word in ["urgent", "immediately", "broken", "failing", "security", "worst"]):
        urgency_score += 2
    if ticket["customer_tier"] in ["premium", "enterprise"]:
        urgency_score += 1
    if ticket["monthly_revenue"] > 10000:
        urgency_score += 1
    if ticket["previous_tickets"] > 10:
        urgency_score += 1

    return "high" if urgency_score >= 4 else "medium" if urgency_score == 3 else "low"
