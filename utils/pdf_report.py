from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_pdf(
    summary,
    monthly_summary,
    recommendations,
    anomalies,
    filename="Financial_Report.pdf"
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    # ============================
    # Title
    # ============================

    story.append(
        Paragraph(
            "<b>Smart Expense Analyzer Report</b>",
            styles["Title"]
        )
    )

    story.append(Paragraph("<br/>", styles["BodyText"]))

    # ============================
    # Financial Summary
    # ============================

    story.append(Paragraph("<b>Financial Summary</b>", styles["Heading2"]))

    story.append(
        Paragraph(
            f"Income: Rs.{summary['Income']:,.2f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Expense: Rs.{summary['Expense']:,.2f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Savings: Rs.{summary['Savings']:,.2f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Transactions: {summary['Transactions']}",
            styles["BodyText"]
        )
    )

    story.append(Paragraph("<br/>", styles["BodyText"]))

    # ============================
    # Monthly Summary Table
    # ============================

    story.append(
        Paragraph(
            "<b>Monthly Financial Summary</b>",
            styles["Heading2"]
        )
    )

    table_data = [["Month", "Income", "Expense"]]

    for _, row in monthly_summary.iterrows():

        table_data.append([
            str(row["Month"]),
            f"Rs.{row['Income']:,.2f}",
            f"Rs.{row['Expense']:,.2f}"
        ])

    table = Table(table_data)

    table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),

        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        ("BACKGROUND", (0, 1), (-1, -1), colors.beige)

    ]))

    story.append(table)

    story.append(Paragraph("<br/>", styles["BodyText"]))

    # ============================
    # AI Recommendations
    # ============================

    story.append(
        Paragraph(
            "<b>AI Savings Recommendations</b>",
            styles["Heading2"]
        )
    )

    for rec in recommendations:

        story.append(
            Paragraph("• " + rec, styles["BodyText"])
        )

    story.append(Paragraph("<br/>", styles["BodyText"]))

    # ============================
    # Anomalies
    # ============================

    story.append(
        Paragraph(
            "<b>Detected Unusual Transactions</b>",
            styles["Heading2"]
        )
    )

    if anomalies.empty:

        story.append(
            Paragraph(
                "No unusual transactions detected.",
                styles["BodyText"]
            )
        )

    else:

        anomaly_table = [["Date", "Description", "Amount", "Category"]]

        for _, row in anomalies.iterrows():

            anomaly_table.append([

                str(row["Date"].date()),

                row["Description"],

                f"Rs.{abs(row['Amount']):,.2f}",

                row["Category"]

            ])

        table = Table(anomaly_table)

        table.setStyle(TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.red),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),

            ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

            ("BACKGROUND", (0, 1), (-1, -1), colors.lavender)

        ]))

        story.append(table)

    # ============================
    # Build PDF
    # ============================

    doc.build(story)

    return filename
    st.markdown("---")
    st.caption("© 2026 Smart Expense Analyzer | Developed using Streamlit & Python")