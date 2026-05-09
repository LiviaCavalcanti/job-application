"""## 2. Cohort Retention Matrix — Medium

Given an events table with `user_id`, `event_date`, `event_type`, compute a retention matrix where:
- rows = cohort (month of first `signup` event)
- columns = months since signup (0, 1, 2, ...)
- values = percentage of cohort still active in that month

**Input DataFrame:**

```
user_id | event_date  | event_type
1       | 2023-01-05  | signup
1       | 2023-02-10  | purchase
2       | 2023-01-20  | signup
2       | 2023-03-01  | purchase
3       | 2023-02-03  | signup
```

**What they're testing:** `groupby` + `transform` for cohort assignment, period arithmetic, `pivot_table`, and normalisation per row. Expect a follow-up asking you to handle users who churn and re-engage.

---
"""