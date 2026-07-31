import plotly.express as px


# ==========================================
# Category-wise Expense Pie Chart
# ==========================================

def category_pie_chart(df):

    expense_df = df[df["Amount"] < 0].copy()

    expense_df["Amount"] = expense_df["Amount"].abs()

    category_data = (
        expense_df.groupby("Category")["Amount"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        category_data,
        names="Category",
        values="Amount",
        title="Expense Distribution by Category",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="<b>%{label}</b><br>Amount: ₹%{value:,.2f}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        font=dict(size=14),
        margin=dict(l=20, r=20, t=60, b=20),
        legend_title="Category"
    )

    return fig


# ==========================================
# Monthly Expense Trend
# ==========================================

def monthly_expense_chart(df):

    expense_df = df[df["Amount"] < 0].copy()

    expense_df["Amount"] = expense_df["Amount"].abs()

    monthly = (
        expense_df.groupby(df["Date"].dt.to_period("M"))["Amount"]
        .sum()
        .reset_index()
    )

    monthly["Date"] = monthly["Date"].astype(str)

    fig = px.line(
        monthly,
        x="Date",
        y="Amount",
        markers=True,
        title="Monthly Expense Trend"
    )

    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8),
        hovertemplate="Month: %{x}<br>Expense: ₹%{y:,.2f}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        xaxis_title="Month",
        yaxis_title="Expense (₹)",
        font=dict(size=14),
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


# ==========================================
# Top Spending Categories
# ==========================================

def top_categories_chart(df):

    expense_df = df[df["Amount"] < 0].copy()

    expense_df["Amount"] = expense_df["Amount"].abs()

    category = (
        expense_df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        category,
        x="Category",
        y="Amount",
        title="Top Spending Categories",
        color="Amount",
        color_continuous_scale="Blues"
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Amount: ₹%{y:,.2f}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        xaxis_title="Category",
        yaxis_title="Total Expense (₹)",
        font=dict(size=14),
        margin=dict(l=20, r=20, t=60, b=20),
        coloraxis_showscale=False
    )

    return fig