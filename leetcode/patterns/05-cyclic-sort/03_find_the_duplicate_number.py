class Solution:
    def findDuplicate(self, nums):
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    return nums[i]
            else:
                i += 1
                
        return -1