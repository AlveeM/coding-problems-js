class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        l = 0
        r = n - 1
        
        while l < n - 1 and nums[l] <= nums[l+1]:
            l += 1
            
        if l == n-1: return 0

        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
        
        sub_max = float('-inf')
        sub_min = float('inf')
        for i in range(l, r+1):
            sub_max = max(sub_max, nums[i])
            sub_min = min(sub_min, nums[i])

        while l > 0 and nums[l-1] > sub_min:
            l -= 1
            
        while r < n-1 and nums[r+1] < sub_max:
            r += 1
            
        return r - l + 1