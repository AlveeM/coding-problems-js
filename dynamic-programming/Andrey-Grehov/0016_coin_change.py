import unittest

'''
Problem: Coin change (https://youtu.be/IqAdhHpRu3Y)
	Given an unlimited supply of coins of given denominations,
	find the total number of ways to make a change of size n.

Recurrence Relation
    F(n) = F(n-1) + F(n-3) + F(n-5) + F(n-10); for denominations of 1, 3, 5, 10
'''

def coin_change(n):
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):
        if i >= 1:
            dp[i] += dp[i-1]
        if i >= 3:
            dp[i] += dp[i-3]
        if i >= 5:
            dp[i] += dp[i-5]
        if i >= 10:
            dp[i] += dp[i-10]

    return dp[n]

def coin_change_with_denominations(n, coins):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for coin in coins:
            if i-coin >= 0:
                dp[i] += dp[i-coin]
    return dp[n]

class Test(unittest.TestCase):
    data1 = [
        (0, 1),
        (3, 2),
        (4, 3),
    ] 
    
    data2 = [
        (0, [1, 3, 5, 10], 1),
        (3, [1, 3, 5, 10], 2),
        (4, [1, 3, 5, 10], 3)
    ]

    def test_coin_change(self):
        for (n, expected) in self.data1:
            actual = coin_change(n)
            self.assertEqual(actual, expected)

    def test_coin_change_with_denominations(self):
        for (n, coins, expected) in self.data2:
            actual = coin_change_with_denominations(n, coins)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()