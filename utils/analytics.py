import pandas as pd


def highest_spending_category(df):

    expense_df = df[df["Amount"] < 0].copy()

    expense_df["Amount"] = expense_df["Amount"].abs()

    category = (
        expense_df
        .groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return category.index[0], category.iloc[0]


def largest_transaction(df):

    expense_df = df[df["Amount"] < 0].copy()

    expense_df["Amount"] = expense_df["Amount"].abs()

    largest = expense_df.loc[
        expense_df["Amount"].idxmax()
    ]

    return largest


def average_monthly_expense(df):

    expense_df = df[df["Amount"] < 0].copy()

    expense_df["Amount"] = expense_df["Amount"].abs()

    expense_df["Month"] = (
        expense_df["Date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly = (
        expense_df
        .groupby("Month")["Amount"]
        .sum()
    )

    return monthly.mean()


def average_transaction(df):

    return df["Amount"].abs().mean()


def monthly_summary(df):

    temp = df.copy()

    temp["Month"] = (
        temp["Date"]
        .dt.to_period("M")
        .astype(str)
    )

    income = (
        temp[temp["Amount"] > 0]
        .groupby("Month")["Amount"]
        .sum()
    )

    expense = (
        temp[temp["Amount"] < 0]
        .groupby("Month")["Amount"]
        .sum()
        .abs()
    )

    summary = pd.DataFrame({
        "Income": income,
        "Expense": expense
    }).fillna(0)

    summary["Savings"] = (
        summary["Income"] - summary["Expense"]
    )

    return summary.reset_index()