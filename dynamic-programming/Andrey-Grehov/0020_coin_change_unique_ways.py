import unittest

'''
Link: https://youtu.be/g0VjciqYeDU
Problem: Coin change
	Given an unlimited supply of coins of given denominations,
	find the unique number of ways to make a change of size n.

	Denominations:
    coins = [1, 2, 3, 5]

    Transition Function:
    i >= 1: f[i][1] = f[i-1][1]
    i >= 2: f[i][2] = f[i-1][1] + f[i-2][2]
    i >= 3: f[i][3] = f[i-1][1] + f[i-2][2] + f[i-3][3]
    i >= 5: f[i][5] = f[i-1][1] + f[i-2][2] + f[i-3][3] + f[i-5][5]
'''

'''
n = 3 coins = 1,2,3

No duplicates
for coin in coins:
    for i in range(1, n+1)

coin = [1]

    (1)      (1)      (1)
3 ------ 2 ------ 1 ------ 0

coin = [1,2]

    (1)      (1)     (1)
//------ 2 ------ 1 ------ 0
3
\\------- 1 ------ 0
    (2)     (1)

coin = [1,2,3]

    (1)     (1)      (1)
//------ 2 ------ 1 ------ 0
|
|  (3)
3 ------ 0
|
|
\\------- 1 ------ 0
    (2)       (1)
Answer: 3

With duplicates
for i in range(1, n+1):
    for coin in coins

coins = [1]

     (1)
1 ------- 0

coins = [1,2]

    (1)       (1)
//------- 1 ------- 0
2
\\--------0
    (2)

coins = [1,2,3]

             (1)      (1)
   (1)   //------- 1 ------- 0
//------ 2
3        \\--------0
|              (2)
|  (2)     (1)
|----- 1 ----- 0
|
|  (3)
|----- 0

Answer: 4
'''
def coin_change(n, coins):
    dp = [0] * (n+1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, n+1):
            if i-coin >= 0:
                dp[i] += dp[i-coin]

    return dp[n]

def coin_change_unique_ways(n, coins):
    dp = [[0] * (len(coins) + 1) for _ in range(n+2)]

    for i in range(len(coins)):
        dp[0][i] = 1

    for i in range(n+1):
        for j in range(len(coins)):
            for k in range(j+1):
                if i-coins[k] < 0: 
                    continue
                dp[i][j] += dp[i-coins[k]][k]

        # if i >= 1:
        #     # using coin indices instead of values
        #     dp[i][0] = dp[i-1][0]
        #     dp[i][1] = dp[i-1][0]
        #     dp[i][2] = dp[i-1][0]
        #     dp[i][3] = dp[i-1][0]
        # if i >= 2:
        #     dp[i][1] += dp[i-2][1]
        #     dp[i][2] += dp[i-2][1]
        #     dp[i][3] += dp[i-2][1]
        # if i >= 3:
        #     dp[i][2] += dp[i-3][2]
        #     dp[i][3] += dp[i-3][2]
        # if i >= 5:
        #     dp[i][3] += dp[i-5][3]

    return dp[n][len(coins)-1]

class Test(unittest.TestCase):    
    data = [
        (75, [1, 2, 3, 5], 2894),
        (75, [2, 3, 5], 107),
        (10, [4, 1], 3),
    ]

    def test_coin_change_unique_ways(self):
        for (n, coins, expected) in self.data:
            actual = coin_change_unique_ways(n, coins)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()