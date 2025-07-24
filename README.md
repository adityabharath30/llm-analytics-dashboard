# 🧠 LLM Analytics Dashboard

A lightweight observability tool for LLM-based applications.  
It captures and visualizes prompt logs, model responses, token usage, latency, and cost — all in a clean Streamlit dashboard.

---

## 🔍 Why This Exists

Most LLM apps today lack visibility into what's really happening with prompts, models, and API usage.  
This project helps developers:
- Track and debug prompts
- Monitor model cost and performance
- Compare prompt versions
- Prepare for production scaling

---

## 🚀 Features

- 📝 Log prompts, responses, latency, token usage, and cost
- 🧪 Mock mode for development (no API key required)
- 📊 Streamlit dashboard with live charts and filters
- 💾 Supports SQLite (local dev) and PostgreSQL (production)
- 🔐 Uses `.env` for secure API key and DB config

---

## 📦 Tech Stack

- **Python**
- **OpenAI API (optional)**
- **SQLAlchemy**
- **Streamlit**
- **SQLite / PostgreSQL**
- **dotenv**

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/llm-analytics-dashboard.git
cd llm-analytics-dashboard
