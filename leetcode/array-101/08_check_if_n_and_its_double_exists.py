from typing import List

# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         nums = {}

#         for num in arr:
#             nums[num] = nums.get(num, 0) + 1

#         for num in arr:
#             if num != 0 and num * 2 in nums:
#                 return True
#             if num == 0 and nums[0] >= 2:
#                 return True

#         return False

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = {}

        for num in arr:
            if num * 2 in nums:
                return True

            if num / 2 in nums:
                return True

            nums[num] = True

        return False