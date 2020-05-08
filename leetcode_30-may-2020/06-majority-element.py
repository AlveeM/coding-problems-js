# Moore's Voting Algorithm
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        idx = 0
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[idx]:
                count += 1
            else:
                count -= 1

            if count == 0:
                idx = i
                count = 1

        return nums[idx]



## Hash map solution ##
# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: [int]) -> int:
#         count = Counter(nums)
#         for num in nums:
#             if count[num] > len(nums)//2:
#                 return num



## Sort Solution ##
# class Solution:
#     def majorityElement(self, nums: [int]) -> int:
#         mid_el_idx = len(nums) // 2
#         nums.sort()
#         return nums[mid_el_idx]