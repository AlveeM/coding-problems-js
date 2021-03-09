class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf') for _ in range(amount+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(n+1):
            for j in range(amount+1):
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(1 + dp[i][j-coins[i-1]], dp[i-1][j])
        
        return dp[n][amount] if dp[n][amount] != float('inf') else -1

# optimized solution
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(amount-coin+1):
                dp[i+coin] = min(dp[i+coin], dp[i]+1)
        return dp[amount] if dp[amount] != float('inf') else -1