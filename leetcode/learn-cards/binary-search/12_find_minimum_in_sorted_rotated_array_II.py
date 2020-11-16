class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
                
        return nums[l]