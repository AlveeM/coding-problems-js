class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        
        first = self.binarySearch(nums, target, True)
        last = self.binarySearch(nums, target, False)
        
        res[0] = first
        res[1] = last
        
        return res
        
    def binarySearch(self, nums, target, first):
        l = 0
        r = len(nums) - 1
        idx = -1
        
        while l <= r:
            m = l + (r - l) // 2
            num = nums[m]
            
            if num < target:
                l = m + 1
            elif num > target:
                r = m - 1
            else:
                idx = m
                if first:
                    r = m - 1
                else:
                    l = m + 1
                
        return idx