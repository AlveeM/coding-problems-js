class Solution:
    def findDisappearedNumbers(self, nums):
        i = 0
        n = len(nums)
        
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        missing = []
        for i, num in enumerate(nums):
            if num != i + 1:
                missing.append(i + 1)
        
        return missing