# Interview Study Guide

## Algorithm Patterns

### 1. Monotonic Stack
**When to use:** "Next greater/smaller element", visibility, blocking, stock span problems.

| Concept | Detail |
|---------|--------|
| Structure | Decreasing stack, process right to left |
| Pop | Each popped element = one visible/reachable item |
| Stack top after pop | First taller/larger element (blocks the rest) |
| Complexity | O(n) — each element pushed and popped at most once |

**Problems:** Visible People in Queue, Daily Temperatures, Stock Span, Largest Rectangle in Histogram

**Template:**
```python
stack = []
for i in range(n - 1, -1, -1):
    count = 0
    while stack and stack[-1] < arr[i]:
        stack.pop()
        count += 1
    if stack:
        count += 1
    answer[i] = count
    stack.append(arr[i])
```

---

### 2. Sort + Sweep (Intervals)
**When to use:** Merge, insert, intersect intervals; meeting rooms; scheduling.

| Concept | Detail |
|---------|--------|
| Step 1 | Sort by start (or end for greedy removal) |
| Step 2 | Sweep left to right, maintain "active" interval |
| Step 3 | Decide: merge with active or start new |
| Complexity | O(n log n) sorting + O(n) sweep |

**Problems:** Merge Intervals, Meeting Rooms I/II, Non-overlapping Intervals, Interval Intersection

**Template:**
```python
intervals.sort()
result = [intervals[0]]
for start, end in intervals[1:]:
    if start <= result[-1][1]:
        result[-1][1] = max(result[-1][1], end)
    else:
        result.append([start, end])
```

---

### 3. Prefix Sum + Hash Map
**When to use:** Subarray sum equals K, contiguous subarray problems.

| Concept | Detail |
|---------|--------|
| Key insight | If `prefix_sum - k` was seen before → subarray sums to k |
| Store | Hash map of {prefix_sum: count} |
| Complexity | O(n) time, O(n) space |

**Template:**
```python
prefix = 0
seen = {0: 1}
count = 0
for num in arr:
    prefix += num
    if prefix - k in seen:
        count += seen[prefix - k]
    seen[prefix] = seen.get(prefix, 0) + 1
```

---

### 4. Dynamic Programming (Knapsack)
**When to use:** Maximize/minimize value with capacity constraints; subset selection under budget.

| Concept | Detail |
|---------|--------|
| 0/1 Knapsack | `dp[i][w] = max(skip, take if fits)` |
| With cardinality | Add dimension: `dp[i][c][b]` (items, count, budget) |
| Greedy fails when | Items have both cost and value — greedy picks suboptimal |
| Complexity | O(n × capacity) or O(n × k × budget) |

---

### 5. Stack (Bracket Matching)
**When to use:** Valid parentheses, expression parsing, nested structures.

| Concept | Detail |
|---------|--------|
| Push | Opening brackets |
| Pop + check | Closing brackets must match top |
| Valid if | Stack empty at end |
| Complexity | O(n) |

---

### 6. Heap (Priority Queue)
**When to use:** Top-K, sliding window median, weighted sampling from streams.

| Concept | Detail |
|---------|--------|
| Two-heap median | Max-heap (lower half) + min-heap (upper half) |
| Weighted reservoir | Key = u^(1/w), min-heap of size k |
| Top-K frequent | (-freq, word) tuples in heap |
| Complexity | O(n log k) |

---

### 7. Sparse Matrix Optimization
**When to use:** Matrix operations where most entries are zero.

| Concept | Detail |
|---------|--------|
| Representation | Dict `{(row, col): value}` — only non-zeros |
| Key optimization | Pre-group B by row, iterate only A's non-zeros |
| Formula | `C[i,k] = Σ_j A[i,j] * B[j,k]` |
| Complexity | O(nnz_A × avg_B_row_density) vs O(n³) brute force |

---

## SQL Patterns

### Gap and Island (Session Attribution)
**When to use:** Sessionization, grouping consecutive rows by gap threshold.

| Step | SQL |
|------|-----|
| 1. Previous row | `LAG(event_ts) OVER (PARTITION BY user ORDER BY ts)` |
| 2. Flag boundaries | `CASE WHEN gap > 30 min THEN 1 ELSE 0` |
| 3. Assign group ID | `SUM(flag) OVER (PARTITION BY user ORDER BY ts)` |
| 4. Aggregate | `GROUP BY user, session_id` |

---

## Pandas Patterns

### Groupby + Aggregation
```python
df.groupby('category')['revenue'].sum().sort_values(ascending=False)
df.groupby('region')['shipping'].mean()
```

### Multi-table Joins
```python
merged = orders.merge(customers, on='customer_id', how='left')
```

### Statistical Testing
```python
from scipy.stats import ttest_ind
t_stat, p_val = ttest_ind(group_a, group_b)
# p < 0.05 → significant difference
```

### Vectorized Feature Engineering
```python
df['rolling_mean'] = df.groupby('sensor')['value'].transform(
    lambda x: x.shift(1).rolling(window).mean()
)
# shift(1) avoids data leakage
```

---

## Probability & Statistics

| Concept | Formula |
|---------|---------|
| **Bayes' theorem** | P(A\|B) = P(B\|A) × P(A) / P(B) |
| **Total probability** | P(B) = Σ P(B\|Aᵢ) × P(Aᵢ) |
| **Binomial** | P(X=k) = C(n,k) × p^k × (1-p)^(n-k) |
| **KS statistic** | max \|CDF_sample - CDF_reference\| |
| **PSI** | Σ (actual% - expected%) × ln(actual% / expected%) |

---

## ML Concepts

| Topic | Key Points |
|-------|-----------|
| **Overfitting signs** | High train acc, low val acc → regularize, more data, dropout |
| **Churn metric (imbalanced)** | F1 > AUC > accuracy; recall on minority class matters |
| **Bagging** | Parallel, reduces variance (Random Forest) |
| **Boosting** | Sequential, reduces bias, adaptive weighting (XGBoost, AdaBoost) |
| **NDCG@k** | DCG = Σ(2^rel - 1) / log₂(i+2); normalize by ideal DCG |

---

## Complexity Cheat Sheet

| Complexity | Patterns |
|-----------|----------|
| O(1) | Bayes, single formula |
| O(n) | Stack, hash map, prefix sum, run-length encoding |
| O(n log n) | Sort-based (intervals), heap top-K |
| O(n log k) | Sliding window median, rolling stats, weighted reservoir |
| O(n × m) | DP tables, sparse matrix |
| O(n × k × B) | Multi-dimensional DP (knapsack + cardinality) |

---

## File Index

| File | Problem | Pattern |
|------|---------|---------|
| `array/number_visible_people_queue.py` | Visible people in queue | Monotonic stack |
| `array/merge_intervals.py` | Merge overlapping intervals | Sort + sweep |
| `array/suarray_sum.py` | Subarray sum = K | Prefix sum + hash map |
| `array/count_duplicates.py` | Count element frequencies | Hash map |
| `sparse_matrix_mult.py` | Sparse matrix multiplication | Pre-group + iterate non-zeros |
| `valid_parenthesis.py` | Valid parentheses | Stack |
| `weighted_reservoir.py` | Weighted reservoir sampling | Heap + A-Res algorithm |
| `word_frequency.py` | Top-K frequent words | Heap / sorting |
| `dp/backpack.py` | 0/1 Knapsack | DP table |
| `dp/topkclosestpoints.py` | Top-K closest under budget | DP + cardinality constraint |
| `sql/session_attribution.py` | Session attribution | Gap and island (SQL) |
| `pandas/claude.py` | Churn prediction | ML pipeline |
| `pandas/cohort_retention_matrix.py` | Cohort retention | Groupby + pivot |
| `pandas/slidewindow.py` | Sliding window median | Two-heap |
| `probability/rolling_zscore.py` | Rolling Z-score anomaly | Vectorized pandas |
| `detectdatadrift.py` | Data drift detection | KS + PSI |
| `implementbdcg.py` | NDCG@k ranking metric | DCG normalization |
| `bayes.py` | Bayes probability | Total probability |
| `probability/prob.py` | Binomial probability | C(n,k) × p^k |
| `string/encode_string.py` | Run-length encoding | Escape sequences |
| `codesignal/questions_and_answers.py` | CodeSignal mock (15 Qs) | Pandas + SQL |
