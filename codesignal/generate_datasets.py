"""
CodeSignal Mock Test - Dataset Generator
Run this first to create all CSV files used in the test.
"""

import pandas as pd
import numpy as np

np.random.seed(42)

# ─────────────────────────────────────────────
# SECTION 1 – Single table: e-commerce orders
# ─────────────────────────────────────────────

n = 500
categories = ["Electronics", "Clothing", "Books", "Home & Garden", "Sports"]
regions = ["North", "South", "East", "West"]
statuses = ["Completed", "Returned", "Pending", "Cancelled"]

orders = pd.DataFrame({
    "order_id": [f"ORD{str(i).zfill(4)}" for i in range(1, n+1)],
    "customer_id": np.random.randint(1001, 1200, n),
    "order_date": pd.date_range("2023-01-01", periods=n, freq="14h").strftime("%Y-%m-%d"),
    "category": np.random.choice(categories, n, p=[0.30, 0.25, 0.15, 0.15, 0.15]),
    "region": np.random.choice(regions, n),
    "quantity": np.random.randint(1, 10, n),
    "unit_price": np.round(np.random.uniform(5, 500, n), 2),
    "discount_pct": np.random.choice([0, 5, 10, 15, 20], n, p=[0.4, 0.2, 0.2, 0.1, 0.1]),
    "status": np.random.choice(statuses, n, p=[0.65, 0.10, 0.15, 0.10]),
    "shipping_days": np.random.randint(1, 14, n),
})

orders["revenue"] = np.round(
    orders["quantity"] * orders["unit_price"] * (1 - orders["discount_pct"] / 100), 2
)

orders.to_csv("./codesignal/orders.csv", index=False)
print("✅ orders.csv created:", len(orders), "rows")

# ─────────────────────────────────────────────
# SECTION 2 – Multi-table: SaaS platform
# ─────────────────────────────────────────────

# Table 1: customers
n_customers = 200
plans = ["Free", "Starter", "Pro", "Enterprise"]
industries = ["Tech", "Finance", "Healthcare", "Retail", "Education"]

customers = pd.DataFrame({
    "customer_id": range(1, n_customers + 1),
    "company_name": [f"Company_{i}" for i in range(1, n_customers + 1)],
    "industry": np.random.choice(industries, n_customers),
    "plan": np.random.choice(plans, n_customers, p=[0.3, 0.3, 0.25, 0.15]),
    "signup_date": pd.date_range("2021-01-01", periods=n_customers, freq="3d").strftime("%Y-%m-%d"),
    "country": np.random.choice(["US", "UK", "DE", "FR", "BR"], n_customers, p=[0.4, 0.2, 0.15, 0.15, 0.1]),
    "churned": np.random.choice([0, 1], n_customers, p=[0.78, 0.22]),
})
customers.to_csv("./codesignal/customers.csv", index=False)
print("✅ customers.csv created:", len(customers), "rows")

# Table 2: subscriptions
plan_prices = {"Free": 0, "Starter": 29, "Pro": 99, "Enterprise": 499}
subscriptions = customers[["customer_id", "plan"]].copy()
subscriptions["monthly_fee"] = subscriptions["plan"].map(plan_prices)
subscriptions["contract_months"] = np.random.choice([1, 6, 12, 24], n_customers, p=[0.2, 0.3, 0.35, 0.15])
subscriptions["start_date"] = pd.date_range("2021-01-01", periods=n_customers, freq="3d").strftime("%Y-%m-%d")
subscriptions["auto_renew"] = np.random.choice([True, False], n_customers, p=[0.7, 0.3])
subscriptions.to_csv("./codesignal/subscriptions.csv", index=False)
print("✅ subscriptions.csv created:", len(subscriptions), "rows")

# Table 3: support_tickets
n_tickets = 600
tickets = pd.DataFrame({
    "ticket_id": range(1, n_tickets + 1),
    "customer_id": np.random.choice(customers["customer_id"], n_tickets),
    "created_date": pd.date_range("2022-01-01", periods=n_tickets, freq="12h").strftime("%Y-%m-%d"),
    "category": np.random.choice(["Bug", "Feature Request", "Billing", "Account", "Performance"], n_tickets),
    "priority": np.random.choice(["Low", "Medium", "High", "Critical"], n_tickets, p=[0.3, 0.4, 0.2, 0.1]),
    "resolved": np.random.choice([1, 0], n_tickets, p=[0.82, 0.18]),
    "resolution_days": np.where(
        np.random.choice([1, 0], n_tickets, p=[0.82, 0.18]) == 1,
        np.random.randint(1, 30, n_tickets),
        np.nan
    ),
    "satisfaction_score": np.random.choice([1, 2, 3, 4, 5, np.nan], n_tickets, p=[0.05, 0.08, 0.15, 0.35, 0.27, 0.10]),
})
tickets.to_csv("./codesignal/support_tickets.csv", index=False)
print("✅ support_tickets.csv created:", len(tickets), "rows")

# Table 4: product_usage
n_usage = 800
features = ["Dashboard", "Reports", "API", "Integrations", "Export", "Analytics"]
usage = pd.DataFrame({
    "usage_id": range(1, n_usage + 1),
    "customer_id": np.random.choice(customers["customer_id"], n_usage),
    "feature": np.random.choice(features, n_usage),
    "usage_date": pd.date_range("2022-06-01", periods=n_usage, freq="8h").strftime("%Y-%m-%d"),
    "session_minutes": np.round(np.random.exponential(25, n_usage), 1),
    "actions_count": np.random.randint(1, 50, n_usage),
})
usage.to_csv("./codesignal/product_usage.csv", index=False)
print("✅ product_usage.csv created:", len(usage), "rows")

print("\n🎯 All datasets ready in ./codesignal_mock/")
print("Files: orders.csv | customers.csv | subscriptions.csv | support_tickets.csv | product_usage.csv")
