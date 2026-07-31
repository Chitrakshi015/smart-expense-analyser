import pandas as pd


CATEGORY_KEYWORDS = {

    "Food": [
        "swiggy",
        "zomato",
        "restaurant",
        "pizza",
        "burger",
        "cafe",
        "food"
    ],

    "Shopping": [
        "amazon",
        "flipkart",
        "myntra",
        "ajio",
        "shopping"
    ],

    "Transport": [
        "uber",
        "ola",
        "metro",
        "petrol",
        "fuel"
    ],

    "Entertainment": [
        "netflix",
        "spotify",
        "prime",
        "hotstar",
        "movie"
    ],

    "Bills": [
        "electricity",
        "water",
        "gas",
        "bill",
        "recharge"
    ],

    "Income": [
        "salary",
        "bonus",
        "credit",
        "refund"
    ]

}


def detect_category(description):

    if pd.isna(description):
        return "Others"

    description = str(description).lower()

    for category, keywords in CATEGORY_KEYWORDS.items():

        for word in keywords:

            if word in description:
                return category

    return "Others"


def categorize_transactions(df):

    df = df.copy()

    if "Description" in df.columns:

        df["Category"] = df["Description"].apply(detect_category)

    return df