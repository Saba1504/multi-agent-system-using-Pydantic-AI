def route_ticket(ticket, urgency):
    subject = ticket["subject"].lower()
    destination = "general_support"

    if "api" in subject or "error" in subject:
        destination = "technical_team"
    elif "billing" in subject:
        destination = "billing_team"
    elif "feature request" in subject:
        destination = "product_team"
    elif urgency == "high":
        destination = "priority_queue"

    return destination
