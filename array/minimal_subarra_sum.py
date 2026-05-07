"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

def min_subarray_len(target, nums):
    left = 0
    sum_so_far = 0
    window_length = 0
    min_length = float('inf')
    for elem in nums:
        sum_so_far += elem
        window_length += 1
        while sum_so_far >= target:
            min_length = min(min_length, window_length)
            sum_so_far -= nums[left]
            left += 1
            window_length -= 1
            print('window_length', window_length, 'sum_so_far', sum_so_far)


    return min_length if min_length != float('inf') else 0
    
print(min_subarray_len(target = 7, nums = [2,3,1,2,4,3]))
print(min_subarray_len(target = 4, nums = [1,4,4]))
print(min_subarray_len(target = 11, nums = [1,1,1,1,1,1,1,1]))
print(min_subarray_len(target = 11, nums = [1,2,3,4,5]))
