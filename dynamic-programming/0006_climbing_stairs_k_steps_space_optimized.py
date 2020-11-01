import unittest

'''
Climbing Stairs (k steps, space optimized)

    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can climb 1..k steps.
    In how many distinct ways can you climb to the top?
'''

# TC: O(nk)
# SC: O(k)
def climb_stairs_k_steps(n, k):
    dp = [0] * k
    dp[0] = 1
    for i in range(1, n+1):
        for j in range (1, k):
            if i - j < 0: continue
            dp[i % k] += dp[(i-j) % k]
    return dp[n % k]

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