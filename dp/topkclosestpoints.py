"""

## 7. Top-K Closest Points Under a Budget — Medium

Given a list of points `(x, y, cost)` and a budget `B`, return the `k` points closest to the origin `(0, 0)` whose **total cost does not exceed B**.

**Input:** `points = [(1,2,3), (3,4,1), (0,1,5), (2,2,2)]`, `B = 6`, `k = 2`
**Output:** `[(0,1,5), (2,2,2)]`

**Constraint:** O(n log k) time. Do not sort all points upfront.

**What they're testing:** This is a knapsack-flavoured heap problem. A naive solution sorts all points by distance then greedily picks within budget — but that's wrong (closer point might be expensive). The correct approach is either a branch-and-bound or, for the greedy version, recognising the problem requires dynamic programming. Strong candidates flag the greedy failure case immediately.

---
"""
example_points = [(1,2,3), (3,4,1), (0,1,5), (2,2,2)]
B = 6
k = 2


def squared_distance(point):
	x, y, _ = point
	return x * x + y * y


def top_k_closest_under_budget(points, budget, k):
	"""
	Return up to k points minimizing total squared distance to origin
	with total cost <= budget.

	This is an exact knapsack-style DP with cardinality constraint.
	Time: O(n * k * budget), Space: O(n * k * budget) for reconstruction.
	"""
	if k <= 0 or budget < 0 or not points:
		return []

	n = len(points)
	k = min(k, n)

	# dp[i][c][b] = minimal total squared distance using first i points,
	# picking exactly c points with exact spend b.
	inf = float('inf')
	dp = [[[inf] * (budget + 1) for _ in range(k + 1)] for _ in range(n + 1)]
	take = [[[False] * (budget + 1) for _ in range(k + 1)] for _ in range(n + 1)]

	for b in range(budget + 1):
		dp[0][0][b] = 0

	for i in range(1, n + 1):
		x, y, cost = points[i - 1]
		dist2 = x * x + y * y

		for c in range(k + 1):
			for b in range(budget + 1):
				# Option 1: skip point i-1
				best = dp[i - 1][c][b]

				# Option 2: take point i-1
				if c > 0 and b >= cost and dp[i - 1][c - 1][b - cost] != inf:
					cand = dp[i - 1][c - 1][b - cost] + dist2
					if cand < best:
						best = cand
						take[i][c][b] = True

				dp[i][c][b] = best

	# Prefer exactly k picks; if impossible, return best feasible with fewer picks.
	best_c = None
	best_b = None
	best_val = inf

	for c in range(k, -1, -1):
		cur_best_val = inf
		cur_best_b = None
		for b in range(budget + 1):
			if dp[n][c][b] < cur_best_val:
				cur_best_val = dp[n][c][b]
				cur_best_b = b
		if cur_best_val != inf:
			best_c = c
			best_b = cur_best_b
			best_val = cur_best_val
			break

	if best_c is None or best_val == inf:
		return []

	# Reconstruct chosen points.
	result = []
	i, c, b = n, best_c, best_b
	while i > 0 and c >= 0 and b >= 0:
		if take[i][c][b]:
			point = points[i - 1]
			result.append(point)
			b -= point[2]
			c -= 1
		i -= 1

	result.reverse()
	return result


selected = top_k_closest_under_budget(example_points, B, k)
print('Selected points:', selected)
print('Total cost:', sum(p[2] for p in selected))
print('k selected:', len(selected))
