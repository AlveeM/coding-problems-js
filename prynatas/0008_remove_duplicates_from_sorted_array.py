from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        non_dup_idx = 0

        for i in range(len(nums)):
            if nums[i] != nums[non_dup_idx]:
                non_dup_idx += 1
                nums[non_dup_idx] = nums[i]

        return non_dup_idx + 1