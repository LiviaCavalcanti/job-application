"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
import numpy as np
nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]

result = [1] * len(nums)
# for i in range(len(nums)):
#     running_mul = 1
#     for j in range(i+1, len(nums)):
#         running_mul *= nums[j]
    
    
#     for j in range(i):
#         running_mul *= nums[j]
#     result[i] = running_mul

running_mul = nums[0]
for i in range(1, len(nums)):
    result[i] *= running_mul
    running_mul *= nums[i]
    
print(result)
running_mul = nums[-1]
for i in range(len(nums)-2, -1, -1):
    result[i] *= running_mul
    running_mul *= nums[i]
print(result)