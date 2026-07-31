# Smart Expense Analyzer

A CSV-based personal expense analyzer with machine learning: automatic
categorization, monthly insights, savings suggestions, spending-pattern
clustering (K-Means) and anomaly detection (Z-score).

## Tech stack

| Layer | Tool |
|---|---|
| UI / app framework | Streamlit |
| Data handling | pandas, NumPy |
| Machine learning | scikit-learn (`KMeans`, `MinMaxScaler`) |
| Charts | Plotly |

100% Python — no JavaScript/React involved anywhere.

## How it works

1. **CSV upload** — `pandas.read_csv`, with column auto-detection for
   date / description / amount / debit-credit type, so it works with most
   bank export formats.
2. **Categorization** — regex/keyword rules classify each transaction into
   categories (Food & Dining, Groceries, Transport, Shopping, Bills &
   Utilities, Entertainment, Health & Fitness, Education, Income, Other).
3. **Monthly insights** — `groupby` on month, spend vs income, and
   month-over-month % change.
4. **Clustering (unsupervised ML)** — each expense is represented as a
   2D feature vector `[amount, category_frequency]`, scaled with
   `MinMaxScaler`, then grouped into 4 clusters with `KMeans`. Clusters are
   ranked by centroid amount and labeled (e.g. "Frequent small spends",
   "Rare big-ticket spends") so the output is interpretable, not just
   cluster numbers.
5. **Anomaly detection (statistical ML)** — for each category, a Z-score
   is computed per transaction: `(amount - category_mean) / category_std`.
   Transactions with `z > 2` are flagged as unusual.
6. **Savings suggestions** — a rule engine reads the outputs of steps 2-5
   (top category, month-over-month spikes, subscription charges, anomaly
   totals, savings rate) and generates plain-language suggestions.

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

This opens the dashboard at `http://localhost:8501`. Upload a CSV (or click
"Try sample data" to see it working immediately with generated demo
transactions).

## Expected CSV format

Any of these column name variants are auto-detected:

- **Date**: `Date`, `Transaction Date`, ...
- **Description**: `Description`, `Narration`, `Particulars`, `Merchant`, ...
- **Amount**: `Amount`, `Amt`, `Value`, `Debit`, ...
- **Type** (optional): `Type`, `Dr/Cr` — if present, used to tell expenses
  from income; otherwise negative amounts are treated as expenses.

## Possible viva/interview questions this covers

- Why K-Means and not another clustering algorithm? (simple, fast,
  interpretable for low-dimensional numeric features; here k=4 is fixed
  because we want fixed behavioral buckets rather than discovering k)
- Why Z-score for anomaly detection instead of Isolation Forest? (small
  per-category sample sizes, easy to explain, no training needed — a good
  fit for a lightweight rule-augmented ML pipeline)
- How is feature scaling handled? (`MinMaxScaler` on amount and category
  frequency before clustering, since K-Means is distance-based)
- How would you extend this? (per-user budgets, recurring-charge detection
  via string similarity, a proper anomaly model like Isolation Forest once
  more data is available, persistence via a database instead of re-upload)
