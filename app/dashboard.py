import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page Config
st.set_page_config(
    page_title="Smart Reminder Dashboard",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 Smart Reminder Management System")
st.markdown("### AI Style Reminder & Notification Dashboard")

# Upload Section
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=['csv']
)

if uploaded_file is not None:

    uploaded_df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Dataset")

    st.dataframe(uploaded_df, use_container_width=True)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")

page = st.sidebar.selectbox(
    "Choose Section",
    ["Overview", "Analytics", "Reports", "Logs"]
)

# Load Reports
try:
    sent_df = pd.read_csv('outputs/sent_report.csv')
except:
    sent_df = pd.DataFrame()

try:
    failed_df = pd.read_csv('outputs/failed_report.csv')
except:
    failed_df = pd.DataFrame()

# Overview Page
if page == "Overview":

    st.subheader("📊 System Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Emails Sent", len(sent_df))

    with col2:
        st.metric("Failed Emails", len(failed_df))

    with col3:
        st.metric(
            "Updated",
            datetime.now().strftime("%H:%M:%S")
        )

# Analytics Page
elif page == "Analytics":

    st.subheader("📈 Reminder Analytics")

    if not sent_df.empty:

        analytics = (
            sent_df['reminder_type']
            .value_counts()
            .reset_index()
        )

        analytics.columns = ['Reminder Type', 'Count']

        chart = px.pie(
            analytics,
            names='Reminder Type',
            values='Count',
            title='Reminder Distribution'
        )

        st.plotly_chart(chart, use_container_width=True)

    else:
        st.warning("No analytics data available.")

# Reports Page
elif page == "Reports":

    st.subheader("📄 Sent Reports")

    if not sent_df.empty:
        st.dataframe(sent_df, use_container_width=True)
    else:
        st.warning("No reports found.")

# Logs Page
elif page == "Logs":

    st.subheader("📝 Failed Logs")

    if not failed_df.empty:
        st.dataframe(failed_df, use_container_width=True)
    else:
        st.success("No failed logs available")

# Footer
st.divider()

st.caption("Built Using Python, Streamlit & Plotly")