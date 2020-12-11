# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums, target):
        res = [-1, -1]
        
        if len(nums) == 0: return res
        if nums[0] > target or nums[-1] < target: return res
        
        first_idx = self.binarySearch(nums, target, True) 
        last_idx = self.binarySearch(nums, target, False)
        
        return [first_idx, last_idx]
        
    def binarySearch(self, nums, target, isFirst):
        idx = -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                idx = mid
                if isFirst:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return idx

class Solution2:
    def searchRange(self, nums, target):
        l = 0
        r = len(nums) - 1
        
        if not nums: return [-1, -1]
        if nums[0] > target or nums[-1] < target: return [-1, -1]
        
        while nums[l] != nums[r]:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                if nums[l] < target:
                    l += 1
                elif nums[r] > target:
                    r -= 1
                    
        if nums[l] == target:
            return [l, r]
        else:
            return [-1, -1]