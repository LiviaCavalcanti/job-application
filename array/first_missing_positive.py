"""
First Missing Positive
=======================

PROBLEM:
  Given an unsorted integer array, return the smallest positive integer
  not present. Must be O(n) time, O(1) auxiliary space.

KEY INSIGHT:
  The answer is ALWAYS in [1, len(nums) + 1].
  Why? n slots can hold at most {1, 2, ..., n}. If all present → answer is n+1.
  This means we only care about values in [1, n] — everything else is noise.

PATTERN: Index-as-Hash (in-place cyclic sort)
  Use the array itself as a boolean/hash map: value v belongs at index v-1.

APPROACHES:

  1. Boolean array O(n) time, O(n) space:
     d = [False] * (n + 1)
     for elem in nums:
         if 1 <= elem <= n:
             d[elem - 1] = True
     Scan d for first False → answer

  2. In-place swap O(n) time, O(1) space:
     While nums[i] is in range [1, n] and not in its home position,
     swap it to index nums[i]-1. Then scan for first mismatch.

WHY THE SWAP LOOP USES while (not for):
  After a swap, nums[i] has a NEW value that might also need placing.
  Only advance i when current value is out of range, duplicate, or in place.

WHY nums[elem-1] != elem (not nums[i] != i+1):
  Prevents infinite loop on duplicates. If the target slot already has
  the correct value, swapping would loop forever.

WHY for...else FOR THE FINAL SCAN:
  If the loop completes without break, all slots match → answer is n+1.
  Without else, you'd overwrite the found answer.

COMPLEXITY:
  - O(n) time: each element swapped at most once to its correct position
  - O(1) space: in-place

TEMPLATE:
  i = 0
  while i < len(nums):
      val = nums[i]
      if 1 <= val <= len(nums) and nums[val - 1] != val:
          nums[val - 1], nums[i] = nums[i], nums[val - 1]
      else:
          i += 1

  for i in range(len(nums)):
      if nums[i] != i + 1:
          return i + 1
  return len(nums) + 1

SIMILAR PROBLEMS:
  - Missing Number (0 to n, one missing)
  - Find All Numbers Disappeared in an Array
  - Find the Duplicate Number
  - Set Mismatch

Example:
  Input:  [3, 4, -1, 1]
  Swaps:  [1, 4, 3, -1] → [1, -1, 3, 4]  (skipping out-of-range -1)
           wait: [-1, 4, 3, 1] → [1, 4, 3, -1] → [1, -1, 3, 4]
  Scan:   index 1 has -1, not 2 → answer = 2
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