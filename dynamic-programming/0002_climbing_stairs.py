import unittest

'''
Problem:
You are climbing a stair case. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Framework for Solving DP Problems:
    1. Define the objective function
        f(i) is the number of distinct ways to reach the i-th stair
    2. Identify base cases
        f(0) = 1 (don't do anything when there's no staircase)
        f(1) = 1
    3. Write down a recurrence relation for the optimized objective function
        f(n) = f(n-1) + f(n-2)
    4. What's the order of execution?
        bottom-up: rely on the values of the previous two subproblems
    5. Where to look for the answer?
        f(n)

Link: https://youtu.be/QlT4HG93Gaw
'''

# TC: O(n)
# SC: O(n)
def climb_stairs(n):
    if (n <= 1): return 1

    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

class Test(unittest.TestCase):
    '''Test Cases: (n, expected)'''
    data = [
        (0, 1),
        (1, 1),
        (3, 3),
        (5, 8)
    ]

    def test_climb_stairs(self):
        for (n, expected) in self.data:
            actual = climb_stairs(n)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()