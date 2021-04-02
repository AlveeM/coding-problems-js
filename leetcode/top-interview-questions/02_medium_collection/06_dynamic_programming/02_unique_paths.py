class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        for r in range(m): 
            dp[r][0] = 1
            
        for c in range(n):
            dp[0][c] = 1
				
        # list comprehension for above code            
        # dp = [[1 if (c == 0 or r == 0) else 0 for c in range(n)] for r in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]
