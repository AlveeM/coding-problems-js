import unittest

'''
Problem: Maximum Profit in a Grid
	A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
    Each cell contains a coin the robot can collect.
	
    What is the maximum profit the robot can accumulate?

	+---+---+---+---+
	| S | 2 | 2 | 1 |
	+---+---+---+---+
	| 3 | 1 | 1 | 1 |
	+---+---+---+---+
	| 4 | 4 | 2 | E |
	+---+---+---+---+
'''

# F(i, j) = max(F(i-1, j), F(i, j-1)) + d(i, j); d -> contains the coin we want to collect
def max_profit(grid):
    m = len(grid)
    n = len(grid[0])
    dp = dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            elif i > 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]

    return dp[m-1][n-1]

class Test(unittest.TestCase):
    '''Test Cases: (grid: List[List[int]], expected: int)'''
    data = [
        (
            [
                [0, 2, 2, 1],
                [3, 1, 1, 1],
                [4, 4, 2, 0]
            ],
            13
        ),
        (
            [
                [0, 2, 2, 50],
                [3, 1, 1, 100],
                [4, 4, 2, 0]
            ],
            154
        )
    ]

    def test_max_profit(self):
        for (grid, expected) in self.data:
            actual = max_profit(grid)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()