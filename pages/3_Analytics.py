import streamlit as st

from utils.insights import calculate_summary
from utils.analytics import (
    highest_spending_category,
    largest_transaction,
    average_monthly_expense,
    average_transaction,
    monthly_summary
)
from utils.anomaly import detect_anomalies
from utils.recommendations import generate_recommendations
from utils.pdf_report import generate_pdf

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Financial Analytics")

# ==========================================
# Check if data exists
# ==========================================

if "transactions" not in st.session_state:
    st.warning("Please upload a CSV first.")
    st.stop()

df = st.session_state["transactions"]

# ==========================================
# Generate Analytics
# ==========================================

dashboard_summary = calculate_summary(df)

category, amount = highest_spending_category(df)
largest = largest_transaction(df)
avg_monthly = average_monthly_expense(df)
avg_transaction = average_transaction(df)

financial_summary = monthly_summary(df)

anomalies = detect_anomalies(df)

recommendations = generate_recommendations(df)

# ==========================================
# Financial Metrics
# ==========================================

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🏆 Highest Spending Category",
        category,
        f"₹{amount:,.2f}"
    )

with col2:
    st.metric(
        "📊 Average Monthly Expense",
        f"₹{avg_monthly:,.2f}"
    )

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "💳 Average Transaction",
        f"₹{avg_transaction:,.2f}"
    )

with col4:
    st.metric(
        "💸 Largest Expense",
        f"₹{abs(largest['Amount']):,.2f}"
    )

st.caption(
    f"{largest['Description']} • {largest['Date'].date()}"
)

# ==========================================
# Monthly Financial Summary
# ==========================================

st.divider()

st.subheader("📅 Monthly Financial Summary")

st.dataframe(
    financial_summary,
    use_container_width=True
)

# ==========================================
# Anomaly Detection
# ==========================================

st.divider()

st.subheader("⚠️ Detected Unusual Transactions")

if anomalies.empty:

    st.success("No unusual transactions detected.")

else:

    display = anomalies[
        ["Date", "Description", "Amount", "Category"]
    ].copy()

    display["Amount"] = display["Amount"].abs()

    st.dataframe(
        display,
        use_container_width=True
    )

# ==========================================
# AI Recommendations
# ==========================================

st.divider()

st.subheader("💡 AI Savings Recommendations")

for recommendation in recommendations:
    st.info(recommendation)

# ==========================================
# PDF Report
# ==========================================

st.divider()

st.subheader("📄 Export Financial Report")

if st.button("Generate PDF Report"):

    filename = generate_pdf(
        dashboard_summary,
        financial_summary,
        recommendations,
        anomalies
    )

    with open(filename, "rb") as pdf_file:

        st.download_button(
            label="⬇ Download Financial Report",
            data=pdf_file,
            file_name=filename,
            mime="application/pdf"
        )

    st.success("✅ PDF generated successfully! Click the button above to download it.")

st.markdown("---")
st.caption("© 2026 Smart Expense Analyzer | Developed using Streamlit & Python")