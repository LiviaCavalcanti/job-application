"""
Write a program that computes the maximum profit that can be made by buying and selling a share
at most twice. The second buy must be made on another date after the first sale.
elements of PROgramming interviews in python
"""

def buy_sell_twice(prices):
    min_so_far = float('inf')
    max_profif = - float('inf')

    forward_profit = []
    for i in range(len(prices)):
        min_so_far = min(min_so_far, prices[i])
        # max_profif = max(max_profif, prices[i] - min_so_far)
        forward_profit.append(prices[i] - min_so_far)
        print(forward_profit)

    max_so_far = -float('inf')
    for i in range(len(prices)-2, -1, -1):
        max_so_far = max(max_so_far, prices[i])
        max_profif = max(max_profif, forward_profit[i-1] + (max_so_far-prices[i]))
    
    return max_profif

stock_price = [12,11,1.3,9,12,8,14,1,3,15]

print(buy_sell_twice(stock_price))