"""
Given an unsorted integer array nums. 
Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
"""

from numpy import inf


min_int = inf
nums = [3,4,1]
# Approach 1: sort and scan O(n log n) time, O(1) space
# d = {}
# for elem in range(len(nums) +2):
#     d[elem]= False
# print(d)
# for i in range(len(nums)):
#     d[nums[i]] = True

# for i in range(1, len(nums) +2):
#     if d[i] == False:
#         min_int = i
#         break
# print(min_int)

# Approach 2: use array as hash map, O(n) time, O(1) space
# d = [False] * (len(nums) + 2)
# for elem in nums:
#     if 1 <= elem <= len(nums):
#         d[elem-1] = True

# for i in range(len(d)):
#     if d[i] == False:
#         min_int = i + 1
#         break
# print(min_int)
nums = [1]
i = 0
while i < len(nums):
    elem = nums[i]
    print(elem)
    if 1 <= elem <= len(nums) and nums[elem-1] != elem:
        nums[elem-1], nums[i] = nums[i], nums[elem-1]
    else:
        i += 1
    print(nums)

for i in range(len(nums)):
    if nums[i] != i + 1:
        min_int = i + 1
        print(min_int)
        break

min_int = len(nums) + 1

def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            elem = nums[i]
            if 1 <= elem <= len(nums) and nums[elem-1] != elem:
                nums[elem-1], nums[i] = nums[i], nums[elem-1]
            else:
                i+= 1 
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i+1
        return len(nums) + 1