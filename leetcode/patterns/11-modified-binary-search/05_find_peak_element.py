class Solution:
    def findPeakElement(self, nums):
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = ((l + r) // 2) + 1
            if nums[mid-1] > nums[mid]:
                r = mid - 1
            else:
                l = mid
                
        return l