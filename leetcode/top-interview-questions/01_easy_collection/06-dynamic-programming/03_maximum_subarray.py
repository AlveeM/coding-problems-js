class Solution:
    def maxSubArray(self, nums):
        if not nums: return 0
        
        dp = [nums[0]]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            next_num = max(dp[i-1] + num, num)
            max_sum = max(max_sum, next_num)
            dp.append(next_num)
            
        return max_sum