import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="LLM Analytics Dashboard", layout="wide")
st.title("🧠 LLM Analytics Dashboard")

# Connect to SQLite DB
conn = sqlite3.connect("logs.db")
df = pd.read_sql_query("SELECT * FROM prompt_logs ORDER BY timestamp DESC", conn)
conn.close()

# Show total count
st.metric(label="Total Logged Prompts", value=len(df))

# Filter UI
with st.sidebar:
    st.header("🔍 Filter Logs")
    model = st.selectbox("Model", options=["All"] + sorted(df["model"].unique().tolist()))
    if model != "All":
        df = df[df["model"] == model]

# Show log table
st.subheader("📄 Prompt Logs")
st.dataframe(df, use_container_width=True)

# Charts
st.subheader("📊 Token Usage Over Time")
st.line_chart(df.set_index("timestamp")[["tokens"]])

st.subheader("💵 Cost Over Time")
st.line_chart(df.set_index("timestamp")[["cost"]])

st.subheader("⚡ Latency Over Time (ms)")
st.line_chart(df.set_index("timestamp")[["latency_ms"]])
