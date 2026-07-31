import streamlit as st

from utils.insights import calculate_summary
from utils.charts import (
    category_pie_chart,
    monthly_expense_chart,
    top_categories_chart
)

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Dashboard")

if "transactions" not in st.session_state:
    st.warning("Please upload a CSV first.")
    st.stop()

df = st.session_state["transactions"]

summary = calculate_summary(df)

# ---------------- KPI Cards ---------------- #

st.subheader("📌 Key Financial Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Income",
    f"₹{summary['Income']:,.0f}"
)

col2.metric(
    "💸 Expense",
    f"₹{summary['Expense']:,.0f}"
)

col3.metric(
    "💵 Savings",
    f"₹{summary['Savings']:,.0f}"
)

col4.metric(
    "📄 Transactions",
    summary["Transactions"]
)

st.divider()

# ---------------- Charts ---------------- #

left, right = st.columns(2)

with left:
    st.plotly_chart(
        category_pie_chart(df),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        monthly_expense_chart(df),
        use_container_width=True
    )

st.plotly_chart(
    top_categories_chart(df),
    use_container_width=True
)

st.divider()

st.subheader("📄 Recent Transactions")

st.dataframe(
    df.tail(20),
    use_container_width=True
)

st.markdown("---")
st.caption("© 2026 Smart Expense Analyzer | Developed using Streamlit & Python")