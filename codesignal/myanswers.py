import pandas as pd

show_all = False
show = 2
if show == 1:
    orders_ds = pd.read_csv('orders.csv')
    print("❓ Q1 — Which product category generated the highest total revenue?")
    print(orders_ds.groupby('category')['revenue'].sum().sort_values(ascending=False).head(1))

    print("❓ Q2 — What is the average shipping time (shipping_days) per region?")
    print(orders_ds.groupby('region')['shipping_days'].mean().round(2).sort_values(ascending=False))

    print("   Round to 2 decimal places. Which region is fastest?\n")
    print(orders_ds.groupby('region')['shipping_days'].mean().round(2).sort_values(ascending=True).head(1).index[0])

    print("❓ Q3 — What percentage of orders have status = 'Returned'?")
    print("   Round to 1 decimal place.\n")

    total_orders = len(orders_ds)
    print(len(orders_ds[orders_ds['status'] == 'Returned']) / total_orders * 100)


    print("❓ Q4 — Which region has the highest average order revenue")
    print("   considering only COMPLETED orders?\n")
    completed_orders = orders_ds[orders_ds['status'] == 'Completed']
    print(completed_orders.groupby('region')['revenue'].mean().round(2).sort_values(ascending=False).head(1).index[0])

    print("❓ Q5 — How many unique customers placed more than 3 orders?")
    print("   (Count of customer_ids with order count > 3)\n")

    # print(orders_ds.groupby('customer_id').size())
    count_customers = orders_ds.groupby('customer_id').count()
    count_customers = count_customers[count_customers['order_id'] > 3]
    count_costumers_alternative = orders_ds.groupby('customer_id').size()

    print(len(count_costumers_alternative[count_costumers_alternative>3]))
    print(len(set(count_customers.index)))


    print("❓ Q6 — What is the total revenue lost due to discounts?")
    print("   (i.e. what would revenue have been at 0% discount, minus actual revenue)")
    print("   Round to 2 decimal places.\n")

    print((orders_ds['unit_price'] * orders_ds['quantity'] - orders_ds['revenue']).sum().round(2))


    print("❓ Q7 — For each category, what is the return rate")
    print("   (% of orders with status = 'Returned')? Sort descending.\n")

    category_return_size = orders_ds[orders_ds['status'] == 'Returned'].groupby('category').size()
    category_size = orders_ds.groupby('category').size()

    print((category_return_size / category_size * 100).round(2).sort_values(ascending=False))
    # print(category_return_size.join(category_size)) how to do with a join?

if show == 2:
    # =======================================================================
    print("=" * 65)
    print("  SECTION 2 — Multi-Table Analysis  |  4 CSV files")
    print("=" * 65)

    print("❓ Q8 — What is the total Monthly Recurring Revenue (MRR)")
    print("   per plan? (Join customers + subscriptions, sum monthly_fee)\n")
    customer_df = pd.read_csv('customers.csv')
    subscription_df = pd.read_csv('subscriptions.csv')
    support_df = pd.read_csv('support_tickets.csv')
    usage_df = pd.read_csv('product_usage.csv')
    
    plan_price_df = customer_df[["customer_id", "plan"]].merge(subscription_df[["customer_id", "monthly_fee"]], on='customer_id')
    print(plan_price_df.groupby('plan')['monthly_fee'].sum())

    print("❓ Q9 — What is the churn rate per industry?")
    print("   (% of customers with churned=1, grouped by industry)\n")
    print(customer_df.groupby('industry').apply(lambda x:( 100 * (x['churned']==1).sum() / len(x)).round(2)))


    print("❓ Q10 — Which plan has the highest average satisfaction score")
    print("   in support tickets? (Join customers + tickets, avg satisfaction_score)\n")
    print(customer_df.merge(support_df, on='customer_id').groupby('plan')['satisfaction_score'].mean().round(2).sort_values(ascending=False))

    print("❓ Q11 — Do churned customers have significantly more")
    print("   support tickets than non-churned customers?")
    print("   Use a t-test (alpha=0.05) and report the p-value.\n")

    # get churned and not churned customers
    churned_customers = customer_df[customer_df['churned']==1]
    current_customers = customer_df[customer_df['churned']==0]

    churned_support = churned_customers.merge(support_df, on='customer_id', how='left')
    current_support = current_customers.merge(support_df, on='customer_id', how='left')
    churned_support.groupby('customer_id').count()
    current_ticket_count = current_support.groupby('customer_id')['ticket_id'].count()
    churned_ticket_count = churned_support.groupby('customer_id')['ticket_id'].count()
    from scipy import stats
    exp_pvalue = stats.ttest_ind(current_ticket_count, churned_ticket_count).pvalue 
    if exp_pvalue < 0.05:
        print('Refuse the null hypothesis => different populations')
    else:
        print('There is no difference between the populations')
    
    print("❓ Q12 — Which feature has the highest average session duration")
    print("   among Pro and Enterprise customers only?\n")
    
    print(customer_df[customer_df['plan'].isin( ['Enterprise', 'Pro'])].merge(usage_df, on= 'customer_id').groupby('feature')['session_minutes'].mean().sort_values(ascending=False).head(1))

    print("❓ Q13 — What is the average number of support tickets")
    print("   for customers on annual contracts (contract_months=12)?")
    print("   vs monthly (contract_months=1)? Is the difference significant (t-test)?\n")

    annual_cust = subscription_df[subscription_df['contract_months']==12]
    annual_avg = annual_cust.merge(support_df, on='customer_id').groupby('customer_id').size().mean()
    print(annual_avg)

    mensual_cust = subscription_df[subscription_df['contract_months']==1]
    mensual_avg = mensual_cust.merge(support_df, on='customer_id').groupby('customer_id').size().mean()
    print(mensual_avg)

    statistic, pvalue =stats.ttest_ind(annual_avg, mensual_avg)
    if pvalue < 0.05:
        print('Refuse the null hypothesis => different populations')
    else:
        print('There is no difference between the populations')

    custo = usage_df.groupby('customer_id')['session_minutes'].mean().sort_values(ascending=False).head(3)
    # print(pd.DataFrame(custo).join(customer_df.set_index('customer_id'), on='customer_id')[['session_minutes', 'industry', 'plan']])
    support_cust_df = pd.DataFrame(custo).merge(support_df, on='customer_id', how='left').groupby('customer_id')
    ticket_count_df = pd.DataFrame(support_cust_df.agg('ticket_id').count()).rename(columns={'ticket_id': 'ticket_count'})
    satisf_df = pd.DataFrame(support_cust_df.agg('satisfaction_score').mean())
    print(pd.DataFrame(custo).merge(ticket_count_df, on='customer_id').merge(satisf_df, on='customer_id'))


# nicer way    
# tix_summary = (
#     tickets.groupby("customer_id")
#     .agg(total_tickets=("ticket_id", "count"),
#          avg_satisfaction=("satisfaction_score", "mean"))
#     .round(2)
#     .reset_index()
# )
# usage_summary = (
#     usage.groupby("customer_id")["session_minutes"]
#     .sum()
#     .round(1)
#     .reset_index()
#     .rename(columns={"session_minutes": "total_session_min"})
# )
# ans_q14 = (
#     customers[["customer_id", "plan", "industry"]]
#     .merge(tix_summary, on="customer_id", how="left")
#     .merge(usage_summary, on="customer_id", how="left")
#     .fillna(0)
#     .sort_values("total_session_min", ascending=False)
#     .head(5)
# )


