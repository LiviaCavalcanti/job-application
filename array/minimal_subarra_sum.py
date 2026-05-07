"""
Minimal Subarray Sum
=====================

PROBLEM:
  Given an array of positive integers and a target, return the minimal length
  of a contiguous subarray whose sum >= target. Return 0 if none exists.

PATTERN: Sliding Window (two pointers)
  - Works because all values are POSITIVE → adding increases sum, removing decreases it
  - This monotonicity guarantees the window only needs to expand/shrink, never restart

HOW IT WORKS:
  1. Expand: move right pointer, add element to sum
  2. Shrink: while sum >= target, record window length, subtract left element, move left
  3. The while loop finds the smallest valid window ending at each right position

WHY SHRINK INSIDE A WHILE (not if):
  - After removing one left element, the sum might STILL be >= target
  - Keep shrinking to find the tightest window before expanding again

WHEN TO RECORD min_length:
  - INSIDE the while loop, BEFORE shrinking — that's when the window is valid

COMPLEXITY:
  - O(n) time: left and right each move at most n times total
  - O(1) space: just pointers and sum

WHEN TO USE SLIDING WINDOW:
  - Contiguous subarray/substring problems
  - All values positive (or problem has monotonic property)
  - "Minimum/maximum length" with a sum/count constraint
  - Longest substring with at most K distinct characters
  - Minimum window substring

TEMPLATE:
  left = 0
  window_sum = 0
  min_len = float('inf')
  for right in range(len(nums)):
      window_sum += nums[right]
      while window_sum >= target:
          min_len = min(min_len, right - left + 1)
          window_sum -= nums[left]
          left += 1
  return min_len if min_len != float('inf') else 0

SIMILAR PROBLEMS:
  - Longest Substring Without Repeating Characters
  - Minimum Window Substring
  - Longest Substring with At Most K Distinct Chars
  - Max Consecutive Ones III
  - Fruit Into Baskets

Example:
  Input: target = 7, nums = [2,3,1,2,4,3]
  Output: 2  (subarray [4,3])
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
