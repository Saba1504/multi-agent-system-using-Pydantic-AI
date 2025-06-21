from agents.urgency_detector import detect_urgency
from agents.routing_agent import route_ticket
import json

def process_ticket(ticket):
    urgency = detect_urgency(ticket)
    destination = route_ticket(ticket, urgency)
    return {
        "ticket_id": ticket["ticket_id"],
        "urgency": urgency,
        "routed_to": destination
    }

if __name__ == "__main__":
    with open("evaluation/test_cases.json") as f:
        tickets = json.load(f)

    results = [process_ticket(ticket) for ticket in tickets]

    for r in results:
        print(json.dumps(r, indent=2))
