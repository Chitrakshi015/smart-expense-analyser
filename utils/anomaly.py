from sklearn.ensemble import IsolationForest
import pandas as pd


def detect_anomalies(df):

    expense_df = df[df["Amount"] < 0].copy()

    expense_df["Amount"] = expense_df["Amount"].abs()

    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    expense_df["Anomaly"] = model.fit_predict(
        expense_df[["Amount"]]
    )

    anomalies = expense_df[
        expense_df["Anomaly"] == -1
    ]

    return anomalies