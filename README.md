# LLM Analytics Dashboard

An **LLMOps observability and cost-governance system** for production LLM applications.

This project adds an **application-level telemetry layer** on top of LLM APIs, enabling fine-grained monitoring, debugging, and cost optimization beyond provider-level usage logs.

---

## Motivation

LLM providers expose usage and billing metrics, but these logs lack the **application context** required to operate real-world systems:

- Which prompt version caused a cost spike?
- Which feature or user is driving token usage?
- How does latency vary across models and workflows?
- How do prompt changes impact cost and performance?

This project addresses those gaps by instrumenting LLM calls directly inside the application and surfacing structured analytics through a dedicated dashboard.

---

## What This System Provides

### Application-Level LLM Telemetry
- Prompt and response logging
- Token usage and per-request cost calculation
- Latency tracking per request
- Model and prompt metadata (e.g. version, feature, user)

### Observability & Monitoring
- End-to-end visibility into LLM inference behavior
- KPI views for usage trends, latency distributions, and spend
- Identification of high-cost or slow prompts

### Cost Governance
- Fine-grained cost attribution by model, feature, or workflow
- Enables budgeting, optimization, and cost-aware prompt design

### Production-Oriented Design
- Decoupled logging from inference logic
- Relational storage using PostgreSQL and SQLAlchemy
- Extensible schema to support multiple models and vendors
- Designed to scale from local experimentation to production workloads

---

## Architecture Overview

- **LLM Client Layer**  
  Instrumented OpenAI API calls emit structured telemetry events.

- **Persistence Layer**  
  Logs are stored in PostgreSQL using SQLAlchemy ORM for queryability and durability.

- **Analytics & Visualization**  
  A Streamlit dashboard provides real-time insights into usage, latency, and cost patterns.

---

## How This Differs from Provider Usage Logs

| Provider Usage Logs | LLM Analytics Dashboard |
|--------------------|------------------------|
| Billing-focused | Application-focused |
| Aggregated metrics | Request-level telemetry |
| Limited metadata | Custom metadata (user, feature, prompt version) |
| No prompt visibility | Full prompt/response observability |
| Static dashboards | Custom, extensible analytics |

---

## Tech Stack

- Python
- OpenAI API
- PostgreSQL
- SQLAlchemy
- Streamlit

---

## Use Cases

- Monitoring production LLM applications
- Debugging latency and cost regressions
- Prompt iteration and optimization
- Cost attribution across features or users
- Foundation for prompt experimentation and A/B testing

---

## Future Extensions

- Prompt versioning and experiment tracking
- Alerting on cost or latency anomalies
- Multi-provider support
- Exportable logs for offline analysis
- Integration with existing observability tools
