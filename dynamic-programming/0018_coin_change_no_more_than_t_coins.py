import unittest

'''
Problem: Coin change
	Given an unlimited supply of coins of given denominations,
	find the total number of ways to make a change of size n, by
	using no more than t coins.
'''

def coin_change_no_more_t_coins(n, t, coins):
    dp = [[0] * (t+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(n+1):
        for j in range(t+1):
            if i > 0 and j == 0:
                dp[i][j] = 0
                continue

            if i == 0 and j > 0:
                dp[i][j] = 1
                continue

            for coin in coins:
                if i-coin >= 0:
                    dp[i][j] += dp[i-coin][j-1]

    return dp[n][t]

class Test(unittest.TestCase):    
    data = [
        (3, 5, [1, 2, 3, 5], 4),
    ]

    def test_coin_change_exactly_t_coins(self):
        for (n, t, coins, expected) in self.data:
            actual = coin_change_no_more_t_coins(n, t, coins)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()