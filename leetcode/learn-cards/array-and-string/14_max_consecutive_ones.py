class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
                
        return max(count, max_count)