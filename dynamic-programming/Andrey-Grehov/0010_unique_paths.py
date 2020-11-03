import unittest

'''
Problem: Unique Paths
	
    A robot is located at the top-left corner of a m x n grid (marked 'S' in the diagram below).
	The robot can only move either down or right at any point in time.
	The robot is trying to reach the bottom-right corner of the grid (marked 'E' in the diagram below).
	How many possible unique paths are there?
	+---+---+---+---+
	| S |   |   |   |
	+---+---+---+---+
	|   |   |   |   |
	+---+---+---+---+
	|   |   |   | E |
	+---+---+---+---+
	Above is a 3 x 4 grid. How many possible unique paths are there?
'''

# F(i, j) = F(i-1, j) + F(i, j-1)
def unique_paths(m, n):
    dp = dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]

    return dp[m-1][n-1]

class Test(unittest.TestCase):
    '''Test Cases: (m, n, expected)'''
    data = [
        (1, 1, 1),
        (3, 4, 10)
    ]

    def test_unique_paths(self):
        for (m, n, expected) in self.data:
            actual = unique_paths(m, n)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()