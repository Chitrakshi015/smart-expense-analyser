import streamlit as st
import utils.preprocessing as preprocessing
import utils.categorizer as categorizer

st.set_page_config(
    page_title="Upload Transactions",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Upload Bank Transaction CSV")

st.write("Upload your bank transaction CSV to begin the analysis.")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        # Load data
        df = preprocessing.load_data(uploaded_file)

        # Clean data
        df = preprocessing.clean_data(df)

        # Categorize transactions
        df = categorizer.categorize_transactions(df)

        # Dataset statistics
        stats = preprocessing.get_statistics(df)

        # Save for other pages
        st.session_state["transactions"] = df

        st.success("✅ File uploaded successfully!")

        st.subheader("Transaction Preview")
        st.dataframe(df, use_container_width=True)

        st.divider()

        st.subheader("Category Distribution")
        st.dataframe(df["Category"].value_counts())

        st.divider()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Rows", stats["Rows"])
        col2.metric("Columns", stats["Columns"])
        col3.metric("Missing Values", stats["Missing Values"])
        col4.metric("Duplicate Rows", stats["Duplicate Rows"])

    except Exception as e:
        st.error(f"❌ Error: {e}")