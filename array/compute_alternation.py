"""
Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array
B having the property that B[0] < B[1] >B [2] < B[3] > [4]< B[5] > ...
"""

def alternation(array):
    for i in range(len(array)):
        array[i: i+2] = sorted(array[i:i+2], reverse=not (i%2))
    return array


stock_price = [12,11,1.3,9,12,8,14,1,3,15]

print(alternation(array=stock_price))