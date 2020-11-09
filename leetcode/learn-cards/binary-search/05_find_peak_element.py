class Solution:
    def findPeakElement(self, nums):
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = l + (r - l + 1) // 2

            if nums[mid - 1] > nums[mid]:
                r = mid - 1
            else:
                l = mid
                
        return l