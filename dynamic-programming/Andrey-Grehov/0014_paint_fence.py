import unittest

'''
Problem: Paint Fence With Two Colors
	There is a fence with n posts, each post can be painted with either green or blue color.
	You have to paint all the posts such that no more than two adjacent fence posts have the same color.

	Return the total number of ways you can paint the fence.
'''
# f(i, j) = f(i-1, 1-j) + f(i-2, 1-j)
def paint_fence(n):
    dp = [[0] * 2 for _ in range(n+1)]

    # green = 1
    # blue = 0
    dp[1][0] = 1
    dp[1][1] = 1
    dp[2][0] = 2 # 10, 00; last post is blue so the 1st one can be either green or blue
    dp[2][1] = 2 # 01, 11

    for i in range(3, n+1):
        for j in range(0, 2):
            dp[i][j] = dp[i-1][1-j] + dp[i-2][1-j]

    return dp[n][0] + dp[n][1]

class Test(unittest.TestCase):
    '''Test Cases: (n, expected)'''
    data = [
        (3, 6),
        (4, 10),
        (5, 16)
    ] 

    def test_paint_fence(self):
        for (n, expected) in self.data:
            actual = paint_fence(n)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()