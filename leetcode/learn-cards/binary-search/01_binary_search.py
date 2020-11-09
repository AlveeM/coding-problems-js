class Solution:
    def search(self, nums, target: int):
        l = 0
        r = len(nums)
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        if l < len(nums) and nums[l] == target:
            return l
        else:
            return -1