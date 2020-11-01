import unittest

'''
Climbing Stairs (k steps, space optimized, skip red steps)

	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can climb 1..k steps. You are not allowed to step on red stairs.
	In how many distinct ways can you climb to the top?
'''

# TC: O(nk)
# SC: O(k)
def climb_stairs_k_steps_skip_red(n, k, stairs):
    dp = [0] * k
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, k):
            if i - j < 0: continue
            if stairs[i-1]:
                dp[i % k] = 0
            else:
                dp[i % k] += dp[(i-j) % k]

    return dp[n % k]

class Test(unittest.TestCase):
    '''Test Cases: (n, k, stairs, expected)'''
    data = [
        (7, 3, [False, True, False, True, True, False, False], 2),
    ]

    def test_climb_stairs_k_steps_skip_red(self):
        for (n, k, stairs, expected) in self.data:
            actual = climb_stairs_k_steps_skip_red(n, k, stairs)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()