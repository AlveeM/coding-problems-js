class Solution:
    def missingNumber(self, nums):
        i = 0
        n = len(nums)
        
        while i < n:
            j = nums[i]
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        for i, num in enumerate(nums):
            if i != num:
                return i
            
        return n