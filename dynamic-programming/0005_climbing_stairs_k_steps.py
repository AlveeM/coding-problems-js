import unittest

'''
Climbing Stairs (k steps)

	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can climb 1..k steps.
	In how many distinct ways can you climb to the top?

Framework for Solving DP Problems:
	1. Define the objective function
        f(i) is the number of distinct ways to reach the i-th stair by making 1 to k steps.
    2. Identify the base cases
        f(0) = 1
        f(1) = 1
    3. Write down a recurrence relation for the optimized objective function
        f(n) = f(n-1) + f(n-2) + ... + f(n-k)
    4. What's the order of the function?
        bottom-up
    5. Where to look for the answer?
        f(n)
'''

# TC: O(nk)
# SC: O(n)
def climb_stairs_k_steps(n, k):
    if n <= 1: return 1

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        # dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + ... + dp[i-k]
        for j in range(1, k+1):
            if i - j < 0: continue
            dp[i] += dp[i-j]

    return dp[n]

class Test(unittest.TestCase):
    '''Test Cases: (n, expected)'''
    data = [
        (3, 2, 3),
        (5, 2, 8),
        (3 ,3, 4),
        (5, 3, 13),
    ]

    def test_climb_stairs_k_steps(self):
        for (n, k, expected) in self.data:
            actual = climb_stairs_k_steps(n, k)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()