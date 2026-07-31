def generate_recommendations(df):

    expense_df = df[df["Amount"] < 0].copy()

    expense_df["Amount"] = expense_df["Amount"].abs()

    category_total = (
        expense_df
        .groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    recommendations = []

    top_category = category_total.index[0]
    top_amount = category_total.iloc[0]

    recommendations.append(
        f"Your highest spending category is {top_category}. "
        f"Reducing it by 10% could save about ₹{top_amount*0.10:,.0f}."
    )

    if "Food" in category_total.index:
        recommendations.append(
            "Food expenses are significant. Preparing meals at home more often may reduce costs."
        )

    if "Shopping" in category_total.index:
        recommendations.append(
            "Shopping contributes a large share of your expenses. Consider delaying non-essential purchases."
        )

    if "Entertainment" in category_total.index:
        recommendations.append(
            "Review your entertainment subscriptions and cancel any you no longer use."
        )

    return recommendations