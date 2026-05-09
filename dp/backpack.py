"""
You are given a list of item weights and values, and a maximum budget. 
Return the maximum total value you can carry without exceeding the budget.
"""

weights = [3, 4, 2]
values = [4, 5, 3]
budget = 6
# answer: 8


def knapsack(weights, values, budget):
    n = len(weights)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    print(dp)

    for i in range(1, n + 1):
        
        weight = weights[i-1]
        value = values[i-1]
        print("i, weight, value", i, weight, value)
        for w in range(budget + 1):
            dp[i][w] = dp[i-1][w]
            if w >= weight:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value) 
            
    return dp[n][budget]

print(knapsack(weights, values, budget))