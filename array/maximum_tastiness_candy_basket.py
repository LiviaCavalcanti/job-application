"""
You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

Return the maximum tastiness of a candy basket.
"""

def foo(basket)-> list[int]:
    diffs = []
    for outer_idx in range(len(basket)):
        for inner_idx in range(outer_idx+1, len(basket)):
            diffs.append(abs(basket[inner_idx] - basket[outer_idx]))

    return diffs

def can_make(price, mid, k):
    count = 1
    last_taken = price[0]
    for j in range(1, len(price)):
        if price[j] - last_taken  >= mid:
            last_taken = price[j]
            count += 1
        if count == k:
            return True
    return False

def maximumTastiness(price = [13,5,1,8,21,2], k = 3):
    price = sorted(price)
    
    best_tastiness =  0
    low = 0
    high = max(price) -min(price)
    while low < high:
        mid = (low + high) // 2
        if  can_make(price, mid, k): 
            best_tastiness = mid
            low = mid + 1
        else: 
            high = mid - 1
    
    return best_tastiness
  
print(maximumTastiness())
    