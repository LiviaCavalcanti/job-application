"""
╔══════════════════════════════════════════════════════════════════╗
║         CODESIGNAL MOCK TEST — Questions + Answers               ║
║         70 min | 15 questions | 3 sections                       ║
╚══════════════════════════════════════════════════════════════════╝

HOW TO USE:
  1. Run generate_datasets.py first to create the CSV files
  2. Read each question (marked with ❓)
  3. Try to solve it yourself BEFORE looking at the answer
  4. Answers are below each question, hidden behind a comment block

Run this file to see all answers printed at once:
  python3 questions_and_answers.py
"""

import pandas as pd
import numpy as np
from scipy import stats

# ─── Load datasets ────────────────────────────────────────────────
orders   = pd.read_csv("orders.csv")
customers    = pd.read_csv("customers.csv")
subscriptions = pd.read_csv("subscriptions.csv")
tickets  = pd.read_csv("support_tickets.csv")
usage    = pd.read_csv("product_usage.csv")

print("=" * 65)
print("  SECTION 1 — Single-Table Analysis  |  orders.csv")
print("=" * 65)
print("""
Dataset: orders.csv
A global e-commerce platform tracks all customer orders in a single
table. Each row is one order. The columns are:
  - order_id       : unique order identifier
  - customer_id    : ID of the customer who placed the order
  - order_date     : date the order was placed (YYYY-MM-DD)
  - category       : product category
  - region         : geographic region (North/South/East/West)
  - quantity       : number of units ordered
  - unit_price     : price per unit (USD)
  - discount_pct   : discount applied (0, 5, 10, 15 or 20 %)
  - status         : order status (Completed/Returned/Pending/Cancelled)
  - shipping_days  : number of days taken to ship
  - revenue        : actual revenue = quantity * unit_price * (1 - discount_pct/100)
""")

# ─────────────────────────────────────────────────────────────────
print("❓ Q1 — Which product category generated the highest total revenue?")
print("   (Return the category name and the rounded revenue.)\n")

# ANSWER:
ans_q1 = (
    orders.groupby("category")["revenue"]
    .sum()
    .round(2)
    .sort_values(ascending=False)
)
print("✅ A1:")
print(ans_q1)
print(f"\n   → Top category: {ans_q1.idxmax()} — ${ans_q1.max():,.2f}\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q2 — What is the average shipping time (shipping_days) per region?")
print("   Round to 2 decimal places. Which region is fastest?\n")

ans_q2 = orders.groupby("region")["shipping_days"].mean().round(2).sort_values()
print("✅ A2:")
print(ans_q2)
print(f"\n   → Fastest region: {ans_q2.idxmin()} ({ans_q2.min()} days)\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q3 — What percentage of orders have status = 'Returned'?")
print("   Round to 1 decimal place.\n")

ans_q3 = round(100 * (orders["status"] == "Returned").sum() / len(orders), 1)
print(f"✅ A3: {ans_q3}% of orders were returned\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q4 — Which region has the highest average order revenue")
print("   considering only COMPLETED orders?\n")

ans_q4 = (
    orders[orders["status"] == "Completed"]
    .groupby("region")["revenue"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)
print("✅ A4:")
print(ans_q4)
print(f"\n   → Top region (completed orders): {ans_q4.idxmax()} — ${ans_q4.max():,.2f}\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q5 — How many unique customers placed more than 3 orders?")
print("   (Count of customer_ids with order count > 3)\n")

ans_q5 = (orders.groupby("customer_id")["order_id"].count() > 3).sum()
print(f"✅ A5: {ans_q5} customers placed more than 3 orders\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q6 — What is the total revenue lost due to discounts?")
print("   (i.e. what would revenue have been at 0% discount, minus actual revenue)")
print("   Round to 2 decimal places.\n")

orders["full_price_revenue"] = orders["quantity"] * orders["unit_price"]
ans_q6 = round((orders["full_price_revenue"] - orders["revenue"]).sum(), 2)
print(f"✅ A6: ${ans_q6:,.2f} lost to discounts\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q7 — For each category, what is the return rate")
print("   (% of orders with status = 'Returned')? Sort descending.\n")

ans_q7 = (
    orders.groupby("category")
    .apply(lambda x: round(100 * (x["status"] == "Returned").sum() / len(x), 2), include_groups=False)
    .sort_values(ascending=False)
)
print("✅ A7:")
print(ans_q7)
print()


print("=" * 65)
print("  SECTION 2 — Multi-Table Analysis  |  4 CSV files")
print("=" * 65)
print("""
Datasets:
  customers.csv    — company info, plan, industry, country, churned flag
  subscriptions.csv — plan pricing, contract length, auto-renew
  support_tickets.csv — tickets raised, priority, resolution, satisfaction
  product_usage.csv  — feature usage logs, session time, actions

Key relationships:
  customers.customer_id → subscriptions.customer_id
  customers.customer_id → support_tickets.customer_id
  customers.customer_id → product_usage.customer_id
""")

# ─────────────────────────────────────────────────────────────────
print("❓ Q8 — What is the total Monthly Recurring Revenue (MRR)")
print("   per plan? (Join customers + subscriptions, sum monthly_fee)\n")

df_q8 = customers.merge(subscriptions, on=["customer_id", "plan"])
ans_q8 = df_q8.groupby("plan")["monthly_fee"].sum().sort_values(ascending=False)
print("✅ A8:")
print(ans_q8)
print()

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q9 — What is the churn rate per industry?")
print("   (% of customers with churned=1, grouped by industry)\n")

ans_q9 = (
    customers.groupby("industry")["churned"]
    .mean()
    .mul(100)
    .round(1)
    .sort_values(ascending=False)
)
print("✅ A9 (churn rate % by industry):")
print(ans_q9)
print()

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q10 — Which plan has the highest average satisfaction score")
print("   in support tickets? (Join customers + tickets, avg satisfaction_score)\n")

df_q10 = (
    customers[["customer_id", "plan"]]
    .merge(tickets[["customer_id", "satisfaction_score"]], on="customer_id")
    .dropna(subset=["satisfaction_score"])
)
ans_q10 = df_q10.groupby("plan")["satisfaction_score"].mean().round(2).sort_values(ascending=False)
print("✅ A10:")
print(ans_q10)
print(f"\n   → Best satisfaction: {ans_q10.idxmax()} plan ({ans_q10.max()})\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q11 — Do churned customers have significantly more")
print("   support tickets than non-churned customers?")
print("   Use a t-test (alpha=0.05) and report the p-value.\n")

ticket_counts = tickets.groupby("customer_id")["ticket_id"].count().reset_index()
ticket_counts.columns = ["customer_id", "ticket_count"]
df_q11 = customers[["customer_id", "churned"]].merge(ticket_counts, on="customer_id", how="left").fillna(0)

churned_tickets    = df_q11[df_q11["churned"] == 1]["ticket_count"]
nonchurned_tickets = df_q11[df_q11["churned"] == 0]["ticket_count"]

t_stat, p_val = stats.ttest_ind(churned_tickets, nonchurned_tickets)
print(f"✅ A11:")
print(f"   Mean tickets (churned)     : {churned_tickets.mean():.2f}")
print(f"   Mean tickets (non-churned) : {nonchurned_tickets.mean():.2f}")
print(f"   T-statistic : {t_stat:.4f}")
print(f"   P-value     : {p_val:.4f}")
print(f"   Significant (p < 0.05)? {'YES ✓' if p_val < 0.05 else 'NO ✗'}\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q12 — Which feature has the highest average session duration")
print("   among Pro and Enterprise customers only?\n")

pro_ent = customers[customers["plan"].isin(["Pro", "Enterprise"])][["customer_id"]]
df_q12 = pro_ent.merge(usage, on="customer_id")
ans_q12 = df_q12.groupby("feature")["session_minutes"].mean().round(2).sort_values(ascending=False)
print("✅ A12:")
print(ans_q12)
print(f"\n   → Top feature: {ans_q12.idxmax()} ({ans_q12.max()} min avg)\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q13 — What is the average number of support tickets")
print("   for customers on annual contracts (contract_months=12)?")
print("   vs monthly (contract_months=1)? Is the difference significant (t-test)?\n")

df_q13 = subscriptions.merge(ticket_counts, on="customer_id", how="left").fillna(0)
annual  = df_q13[df_q13["contract_months"] == 12]["ticket_count"]
monthly = df_q13[df_q13["contract_months"] == 1]["ticket_count"]
t2, p2 = stats.ttest_ind(annual, monthly)
print(f"✅ A13:")
print(f"   Mean tickets (annual contract)  : {annual.mean():.2f}")
print(f"   Mean tickets (monthly contract) : {monthly.mean():.2f}")
print(f"   P-value: {p2:.4f} → {'Significant ✓' if p2 < 0.05 else 'Not significant ✗'}\n")

# ─────────────────────────────────────────────────────────────────
print("─" * 65)
print("❓ Q14 — Build a customer health summary table with:")
print("   customer_id | plan | industry | total_tickets | avg_satisfaction | total_session_min")
print("   For the top 5 customers by total session time.\n")

tix_summary = (
    tickets.groupby("customer_id")
    .agg(total_tickets=("ticket_id", "count"),
         avg_satisfaction=("satisfaction_score", "mean"))
    .round(2)
    .reset_index()
)
usage_summary = (
    usage.groupby("customer_id")["session_minutes"]
    .sum()
    .round(1)
    .reset_index()
    .rename(columns={"session_minutes": "total_session_min"})
)
ans_q14 = (
    customers[["customer_id", "plan", "industry"]]
    .merge(tix_summary, on="customer_id", how="left")
    .merge(usage_summary, on="customer_id", how="left")
    .fillna(0)
    .sort_values("total_session_min", ascending=False)
    .head(5)
)
print("✅ A14:")
print(ans_q14.to_string(index=False))
print()


print("=" * 65)
print("  SECTION 3 — SQL  |  1 question")
print("=" * 65)
print("""
Context:
  You have the same orders table as Section 1, available in SQL as `orders`.
  
  The business wants to identify high-value customers at risk of churn.
  A customer is considered 'at risk' if:
    - They have placed at least 2 orders
    - Their return rate (returned orders / total orders) is above 20%
    - Their total revenue is above $500
  
  Return: customer_id, total_orders, returned_orders, return_rate (%), total_revenue
  Sorted by return_rate DESC.
""")
print("""✅ A15 — SQL Answer:

SELECT
    customer_id,
    COUNT(*)                                          AS total_orders,
    SUM(CASE WHEN status = 'Returned' THEN 1 ELSE 0 END) AS returned_orders,
    ROUND(
        100.0 * SUM(CASE WHEN status = 'Returned' THEN 1 ELSE 0 END) / COUNT(*),
        1
    )                                                 AS return_rate,
    ROUND(SUM(revenue), 2)                            AS total_revenue
FROM orders
GROUP BY customer_id
HAVING
    COUNT(*) >= 2
    AND (100.0 * SUM(CASE WHEN status = 'Returned' THEN 1 ELSE 0 END) / COUNT(*)) > 20
    AND SUM(revenue) > 500
ORDER BY return_rate DESC;
""")

# Simulate the SQL in pandas for verification:
sql_sim = (
    orders.groupby("customer_id")
    .agg(
        total_orders=("order_id", "count"),
        returned_orders=("status", lambda x: (x == "Returned").sum()),
        total_revenue=("revenue", "sum"),
    )
    .reset_index()
)
sql_sim["return_rate"] = round(100 * sql_sim["returned_orders"] / sql_sim["total_orders"], 1)
sql_sim["total_revenue"] = sql_sim["total_revenue"].round(2)
ans_q15 = sql_sim[
    (sql_sim["total_orders"] >= 2) &
    (sql_sim["return_rate"] > 20) &
    (sql_sim["total_revenue"] > 500)
].sort_values("return_rate", ascending=False)

print("   (Verified in pandas — first 5 rows:)")
print(ans_q15.head().to_string(index=False))

print("\n" + "=" * 65)
print("  END OF MOCK TEST — Good luck! 🚀")
print("=" * 65)
