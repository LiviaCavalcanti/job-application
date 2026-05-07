"""
Count the number of contiguous subarrays whose sum equals k. 
Example:
Input: nums = [1,1,1], k = 2
Output: 2
"""

nums = [1, 2, 3, 5, 8, 2, 6, 2, 1, 3, 2, 2, 1, 1, 1, 1]
k = 3
def subarray_sum(nums, k):
    count = 0
    current_sum = 0
    sum_freq = {0: 1}  # Initialize with sum 0 occurring once

    for num in nums:
        print("num", num)
        current_sum += num
        print("current_sum", current_sum)
        if (current_sum - k) in sum_freq:
            count += sum_freq[current_sum - k]
            print("count", count)
        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1
        print("sum_freq", sum_freq)

    return count

print(subarray_sum(nums, k))