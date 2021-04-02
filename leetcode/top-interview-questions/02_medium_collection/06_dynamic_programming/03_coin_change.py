class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp table:
        # index denotes the current amount
        # value denotes the minimum number of coins requried to reach amount
        dp = [float('inf') for _ in range(amount + 1)]
        # 0 amount is always possible with 0 coins
        dp[0] = 0
        
        for coin in coins:
            for i in range(amount - coin + 1): # coin + i must be < amount
                cur_amount = i + coin # skips amounts that are less than current denomination
                cur_min = dp[i + coin]
                pos_min = dp[i] + 1 # current minimum coins + 1 coin of current denomination
                dp[cur_amount] = min(pos_min, cur_min)
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]