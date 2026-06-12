"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""

def three_sum(nums: list[int], target: int = 0) -> int:
    three_nums = []
    nums = sorted(nums)
    i = 0
    while i < len(nums):
        val1 = nums[i]
        left = i + 1
        if i > 0 and nums[i] == nums[i-1]:
            # print(i)
            i+=1
            continue
        right = len(nums) -1
        while left < right:
            vals_sum = val1 + nums[left] + nums[right]
            # print(vals_sum)
            if vals_sum > 0:
                right -= 1
            elif vals_sum < 0:
                left += 1
                # print(f"left{left}")
            else:
                three_nums.append([nums[i], nums[left], nums[right]])
                while right > left and nums[right] == nums[right-1]:
                    right -= 1

                while right > left and nums[left] == nums[left+1]:
                    left +=1
                right -= 1
                left += 1
        i +=1
   
            
    return three_nums

print(three_sum([-1,0,1,2,-1,-4], 0))
print(three_sum([-0,0,0,0,0,0], 0))
print(three_sum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]), 0)
print(three_sum([-1,0,1,2,-1,-4]))