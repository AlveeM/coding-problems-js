from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while (left < right):
            mid = (right + left) // 2
            # case 1: mid is even
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    left = mid + 2
                elif nums[mid] == nums[mid-1]:
                    right = mid - 2
                else:
                    return nums[mid]
            # case 2: mid is odd
            else:
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return nums[left]