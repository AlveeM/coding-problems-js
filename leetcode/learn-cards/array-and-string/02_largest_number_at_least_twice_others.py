class Solution:
    def dominantIndex(self, nums):
        max_num = -1
        max_idx = -1
        
        for idx, num in enumerate(nums):
            if num > max_num:
                max_num = num
                max_idx = idx
        
        for num in nums:
            if num != max_num and num * 2 > max_num:
                return -1
            
        return max_idx