class Solution:
    def climbStairs(self, n):
        if n <= 1: return 1
        
        dp = [1, 1]
        for _ in range(2, n+1):
            old = dp[1]
            new = dp[0] + dp[1]
            dp[0] = old
            dp[1] = new

        return dp[-1]