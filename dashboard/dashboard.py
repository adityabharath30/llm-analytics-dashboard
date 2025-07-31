import streamlit as st
import pandas as pd
import altair as alt
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Setup database connection (default = SQLite)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///logs.db")
engine = create_engine(DATABASE_URL)

st.set_page_config(page_title="LLM Analytics", layout="wide")
st.title("🧠 LLM Analytics Dashboard")

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_sql("SELECT * FROM prompt_logs ORDER BY timestamp DESC", engine)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except Exception as e:
        st.error(f"Error loading logs: {e}")
        return pd.DataFrame()

df = load_data()

# Show logs table
st.subheader("📄 Prompt Logs")
if df.empty:
    st.warning("No logs found in the database.")
else:
    st.dataframe(df, use_container_width=True)

    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    model_filter = st.sidebar.multiselect("Model", df['model'].unique(), default=df['model'].unique())
    df_filtered = df[df['model'].isin(model_filter)]

    # Charts
    st.subheader("📊 Token Usage Over Time")
    token_chart = alt.Chart(df_filtered).mark_line(point=True).encode(
        x='timestamp:T',
        y='tokens:Q',
        color='model:N',
        tooltip=['timestamp', 'tokens', 'model']
    ).properties(width=800, height=300)
    st.altair_chart(token_chart, use_container_width=True)

    st.subheader("⚡ Latency Over Time (ms)")
    latency_chart = alt.Chart(df_filtered).mark_line(point=True).encode(
        x='timestamp:T',
        y='latency_ms:Q',
        color='model:N',
        tooltip=['timestamp', 'latency_ms', 'model']
    ).properties(width=800, height=300)
    st.altair_chart(latency_chart, use_container_width=True)

    st.subheader("💵 Cost Over Time ($)")
    cost_chart = alt.Chart(df_filtered).mark_line(point=True).encode(
        x='timestamp:T',
        y='cost:Q',
        color='model:N',
        tooltip=['timestamp', 'cost', 'model']
    ).properties(width=800, height=300)
    st.altair_chart(cost_chart, use_container_width=True)

    st.subheader("📈 Prompt Count by Model")
    model_counts = df_filtered['model'].value_counts().reset_index()
    model_counts.columns = ['model', 'count']
    bar_chart = alt.Chart(model_counts).mark_bar().encode(
        x='model:N',
        y='count:Q',
        color='model:N',
        tooltip=['model', 'count']
    ).properties(width=600)
    st.altair_chart(bar_chart, use_container_width=True)
