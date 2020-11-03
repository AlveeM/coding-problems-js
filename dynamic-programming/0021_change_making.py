import unittest

'''
Problem: Change-making Problem
	Given an unlimited supply of coins of given denominations,
	what is the minimum number of coins needed to make a change of size n?
	
    coins = 1, 3, 5
'''

def change_making(n, coins):
    dp = [None] * (n+1)
    dp[0] = 0

    for i in range(1, n+1):
        dp[i] = float('inf')
        for j in range(len(coins)):
            if i-coins[j] < 0 or 1+dp[i-coins[j]] == float('inf'):
                continue 
            dp[i] = min(dp[i], 1+dp[i-coins[j]])

        # if i >= 1:
        #     dp[i] = min(dp[i], 1+dp[i-1])
        # if i >= 3:
        #     dp[i] = min(dp[i], 1+dp[i-1], 1+dp[i-3])
        # if i >= 5:
        #     dp[i] = min(dp[i], 1+dp[i-1], 1+dp[i-3], 1+dp[i-5])

    if dp[n] == float('inf'):
        return -1

    return dp[n]


class Test(unittest.TestCase):    
    data = [
        (29, [1, 3, 5], 7),
        (1, [2, 3, 5], -1),
        (56, [15, 4, 3], 6),
    ]

    def test_change_making(self):
        for (n, coins, expected) in self.data:
            actual = change_making(n, coins)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()