"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

"""

def buy_sell_stock1(prices):
    
    buy = 0
    sell = len(prices) - 1
    i = 0
    j = len(prices) -2
    while i < j:
        if prices[j] > prices[sell]:
            sell = j
            
        if prices[i] < prices[buy]:
            buy = i
        
        j -= 1
        i += 1

        print(f"i: {i}, j: {j}, buy: {prices[buy]}, sell: {prices[sell]}")

def buy_sell_stock(prices):
    min_sofar = float('inf')
    max_profit = 0
    for value in prices:
        if value - min_sofar > max_profit:
            max_profit = value - min_sofar
            
        if value < min_sofar:
            min_sofar = value
    return max_profit

print(buy_sell_stock([10,5,6, 2,7,1]))
print(buy_sell_stock([10,8,7,5,2]))