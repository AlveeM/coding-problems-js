class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        max_len = 1
        
        # i: current index
        # j: previous index
        for i in range(len(dp)):
            for j in range(i):
                # cond 1: nums[j] < nums[i] as we want an increasing sequence
                # cond 2: dp[j] >= dp[i] to choose LIS if it's bigger
                #         without including the num at current index 
                if nums[j] < nums[i] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
                    max_len = max(dp[i], max_len)
        
        return max_len