from typing import List

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         l_idx = 0
#         r_idx = len(nums) - 1

#         while l_idx <= r_idx:
#             if nums[l_idx] == val:
#                 nums[l_idx], nums[r_idx] = nums[r_idx], nums[l_idx]
#                 r_idx -= 1
#             else:
#                 l_idx += 1

#         return l_idx

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        non_val_count = 0

        for i in range(len(nums)):
            if (nums[i] != val):
                nums[non_val_count] = nums[i]
                non_val_count += 1
            
        return non_val_count