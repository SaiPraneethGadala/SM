"""
Tutor Dashboard — Auto-Updating Student Engagement Monitor
----------------------------------------------------------
Run:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os
import time

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Student Engagement Dashboard",
    layout="wide"
)

st.title("🎓 Student Engagement Dashboard")

LOGS_DIR = "logs"
REFRESH_INTERVAL = 2000  # milliseconds

# ----------------------------
# Auto Refresh
# ----------------------------
try:
    st.autorefresh(
        interval=REFRESH_INTERVAL,
        key="dashboard_refresh"
    )
except Exception:
    pass

# ----------------------------
# Ensure Logs Directory Exists
# ----------------------------
os.makedirs(LOGS_DIR, exist_ok=True)

# ----------------------------
# Load Available CSV Files
# ----------------------------
csv_files = [
    f for f in os.listdir(LOGS_DIR)
    if f.endswith(".csv")
]

if not csv_files:
    st.warning(
        "⚠️ No session logs found.\n\n"
        "Run realtime_monitor.py first."
    )
    st.stop()

# ----------------------------
# Session Selection
# ----------------------------
follow_latest = st.checkbox(
    "📍 Follow Latest Running Session",
    value=True
)

if follow_latest:
    selected_file = max(
        csv_files,
        key=lambda f: os.path.getmtime(
            os.path.join(LOGS_DIR, f)
        )
    )
else:
    selected_file = st.selectbox(
        "Select Session",
        sorted(csv_files, reverse=True)
    )

path = os.path.join(LOGS_DIR, selected_file)

st.info(f"Tracking: **{selected_file}**")

# ----------------------------
# Safe CSV Loader
# ----------------------------
def load_session_data(file_path):
    try:

        if not os.path.exists(file_path):
            return pd.DataFrame()

        if os.path.getsize(file_path) == 0:
            return pd.DataFrame()

        df = pd.read_csv(file_path)

        if df is None:
            return pd.DataFrame()

        return df

    except pd.errors.EmptyDataError:
        return pd.DataFrame()

    except Exception as e:
        st.error(f"Error loading file: {e}")
        return pd.DataFrame()


df = load_session_data(path)

# ----------------------------
# Validate Data
# ----------------------------
if df.empty:
    st.warning(
        "⚠️ Log file exists but contains no data yet.\n\n"
        "Wait for realtime_monitor.py to write entries."
    )
    st.stop()

required_columns = ["timestamp", "label"]

missing = [
    col for col in required_columns
    if col not in df.columns
]

if missing:
    st.error(
        f"Missing required columns: {', '.join(missing)}"
    )
    st.stop()

# ----------------------------
# Manual Refresh
# ----------------------------
col1, col2 = st.columns([5, 1])

with col2:
    if st.button("🔄 Refresh"):
        st.rerun()

# ----------------------------
# Summary Metrics
# ----------------------------
st.subheader("📊 Engagement Summary")

summary = (
    df["label"]
    .value_counts(normalize=True)
    * 100
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Attentive",
    f"{summary.get('Attentive', 0):.1f}%"
)

c2.metric(
    "Confused",
    f"{summary.get('Confused', 0):.1f}%"
)

c3.metric(
    "Distracted",
    f"{summary.get('Distracted', 0):.1f}%"
)

st.divider()

# ----------------------------
# Pie Chart
# ----------------------------
fig_pie = px.pie(
    df,
    names="label",
    title="Engagement Breakdown",
    color="label",
    color_discrete_map={
        "Attentive": "green",
        "Confused": "gold",
        "Distracted": "red"
    }
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

st.divider()

# ----------------------------
# Timeline Chart
# ----------------------------
df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

df = df.dropna(subset=["timestamp"])

timeline = (
    df.groupby(
        ["timestamp", "label"]
    )
    .size()
    .reset_index(name="count")
)

if not timeline.empty:

    fig_line = px.line(
        timeline,
        x="timestamp",
        y="count",
        color="label",
        markers=True,
        title="Engagement Over Time",
        color_discrete_map={
            "Attentive": "green",
            "Confused": "gold",
            "Distracted": "red"
        }
    )

    st.plotly_chart(
        fig_line,
        use_container_width=True
    )

st.divider()

# ----------------------------
# Raw Data
# ----------------------------
with st.expander("📄 View Raw Data"):

    st.dataframe(
        df.tail(100),
        use_container_width=True
    )

# ----------------------------
# Session Info
# ----------------------------
st.subheader("ℹ️ Session Information")

st.write(f"**File:** {selected_file}")
st.write(f"**Records:** {len(df)}")

try:
    last_update = time.ctime(
        os.path.getmtime(path)
    )
    st.write(f"**Last Updated:** {last_update}")
except Exception:
    pass

st.success("✅ Dashboard Running Successfully")