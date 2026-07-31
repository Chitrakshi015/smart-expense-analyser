import pandas as pd


def calculate_summary(df):
    """
    Calculate financial summary from transactions.
    """

    income = df[df["Amount"] > 0]["Amount"].sum()

    expense = abs(df[df["Amount"] < 0]["Amount"].sum())

    savings = income - expense

    total_transactions = len(df)

    return {
        "Income": income,
        "Expense": expense,
        "Savings": savings,
        "Transactions": total_transactions
    }