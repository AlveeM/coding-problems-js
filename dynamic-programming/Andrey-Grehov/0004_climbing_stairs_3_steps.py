import unittest

'''
Climbing Stairs (3 steps)

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1, 2 or 3 steps.
In how many distinct ways can you climb to the top?

Framework for Solving DP Problems:
    1. Define the objective function
        f(i) is the number of distinct ways to reach the i-th stair.
    2. Identify base cases
        f(0) = 1
        f(1) = 1
        f(2) = 2
    3. Write down a recurrence relation for the optimized objective function
        f(n) = f(n-1) + f(n-2) + f(n-3)
    4. What's the order of execution?
        bottom-up
    5. Where to look for the answer?
        f(n)
'''

# TC: O(n)
# SC: O(n)
def climb_stairs_3_steps(n):
    if n <= 1: return 1
    if n == 2: return 2

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

class Test(unittest.TestCase):
    '''Test Cases: (n, expected)'''
    data = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 4),
        (5, 13)
    ]

    def test_climb_stairs_3_steps(self):
        for (n, expected) in self.data:
            actual = climb_stairs_3_steps(n)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()