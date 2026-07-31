import pandas as pd


def load_data(uploaded_file):
    """
    Load CSV file into a pandas DataFrame.
    """
    return pd.read_csv(uploaded_file)


def clean_data(df):
    """
    Clean and preprocess the transaction data.
    """

    # Create a copy to avoid modifying original dataframe
    df = df.copy()

    # Remove duplicate transactions
    df.drop_duplicates(inplace=True)

    # Remove rows where all values are missing
    df.dropna(how="all", inplace=True)

    # Standardize column names
    df.columns = df.columns.str.strip()

    # Convert Date column
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Convert Amount column
    if "Amount" in df.columns:
        df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    return df


def get_statistics(df):
    """
    Return basic dataset statistics.
    """

    return {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    }