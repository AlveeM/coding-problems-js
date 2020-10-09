# https://leetcode.com/problems/two-sum/
from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # declare a variable and initialize it to an empty object (num_obj)
        num_obj = {}
        # iterate over nums
        for i in range(len(nums)):
            # current index -> i
            # current number -> nums[i]
            # declare a variable and set it to target - current num (complement)
            complement = target - nums[i]
            # if complement exists in num_obj
            if complement in num_obj:
                # return an array with the index of the current num and complement
                return [i, num_obj[complement]]
            # add a property current num with value current idx to the num_obj
            num_obj[nums[i]] = i

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         obj = {}
#         for idx, current_num in enumerate(nums):
#             comp = target - current_num
#             if comp in obj:
#                 return [obj[comp], idx]
#             obj[current_num] = idx