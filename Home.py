import streamlit as st

st.set_page_config(
    page_title="Smart Expense Analyzer",
    page_icon="💰",
    layout="wide"
)

with st.sidebar:
    st.title("💰 Smart Expense Analyzer")
    st.markdown("---")
    st.info(
        """
        Navigate using the pages on the left.

        📂 Upload Data

        📊 Dashboard

        📈 Analytics
        """
    )

st.title("💰 Smart Expense Analyzer")

st.markdown("""
Welcome to the **Smart Expense Analyzer**, an AI-powered personal finance dashboard.

This application helps you:

- 📂 Upload your transaction history
- 🧹 Automatically clean and preprocess data
- 🏷 Categorize expenses using AI-inspired rules
- 📊 Visualize spending patterns
- 📈 Analyze monthly financial trends
- 🤖 Detect unusual transactions using Machine Learning
- 💡 Receive personalized savings recommendations
- 📄 Export a professional financial report as PDF
""")

st.divider()

st.subheader("🚀 How to Use")

st.markdown("""
1. Go to **Upload Data**
2. Upload your CSV file
3. Explore the **Dashboard**
4. Visit **Analytics**
5. Generate your PDF Report
""")

st.divider()

st.success("✅ Project developed using Python, Streamlit, Plotly, Pandas, Scikit-learn, and ReportLab.")

st.markdown("---")
st.caption("© 2026 Smart Expense Analyzer | Developed using Streamlit & Python")