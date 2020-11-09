class Solution:
    def searchRange(self, nums, target):
        res = [-1, -1]
        
        first = self.binarySearch(nums, target, True)
        last = self.binarySearch(nums, target, False)
        
        if first != -1:
            res[0] = first
            res[1] = last
            
        return res
        
    def binarySearch(self, nums, target, first):
        idx = -1
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                idx = mid
                if first:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return idx