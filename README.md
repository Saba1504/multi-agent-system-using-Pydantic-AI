# multi-agent-system-using-Pydantic-AI
This project is a multi-agent system that intelligently analyzes and routes customer support tickets using specialized agents. It was developed as part of the Draconic AI Engineer case study challenge.

## 📌 Project Overview

Modern support teams handle thousands of tickets daily. To streamline operations, this system uses **multiple collaborating agents** to:

- Understand ticket **urgency**
- Route tickets to the **right team**
- Handle **edge cases** like vague messages or emotionally intense language

This design improves customer experience by prioritizing and assigning tickets accurately.

Multi-Agent Architecture

1. UrgencyDetectorAgent
- Analyzes ticket urgency using:
  - Emotional tone in the message
  - Customer tier (Free, Premium, Enterprise)
  - Monthly revenue and ticket history
- Returns: `low`, `medium`, or `high` urgency

2. RoutingAgent
- Routes the ticket to one of:
  - `technical_team`
  - `billing_team`
  - `product_team`
  - `priority_queue`
  - `general_support`
- Uses subject keywords + urgency to make decisions

Agents communicate indirectly by passing data between each other in a coordinated pipeline.
├── main.py # Main logic to run agents and output results
├── agents/
│ ├── urgency_detector.py # Agent for urgency classification
│ └── routing_agent.py # Agent for ticket routing
├── evaluation/
│ ├── test_cases.json # Sample test cases
│ └── metrics.py # Evaluation metrics
├── docs/
│ ├── design.md # System design and rationale
│ └── issues.txt # What didn’t work and why
├── ai_chat_history.txt # Full ChatGPT development log
└── README.md
