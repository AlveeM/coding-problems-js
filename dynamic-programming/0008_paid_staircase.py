import unittest

'''
Paid Staircase
	
    You are climbing a paid staircase. It takes n steps to reach to the top and you have to
	pay p[i] to step on the i-th stair. Each time you can climb 1 or 2 steps.
	What's the cheapest amount you have to pay to get to the top of the staircase?

    Framework
    1. Define the objective function
        F(i) -> the minimum cost to get to the i-th stair
    2. Identify the base cases
        F(0) = 0
    3. Write down a recurrence relation for the optimized objective function
        F(n) = P(n) + min(F(n-1), F(n-2))
    4. What's the order of the function?
        Bottom-up
    5. Where to look for the answer?
        F(n)
'''

# TC: O(n)
# SC: O(n)
def paid_staircase(n, p):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = p[1]

    for i in range(2, n+1):
        dp[i] = min(dp[i-1], dp[i-2]) + p[i]

    return dp[n]

class Test(unittest.TestCase):
    '''Test Cases: (n, p, expected)'''
    data = [
        (3, [0, 3, 2, 4], 6),
    ]

    def test_paid_staircase(self):
        for (n, p, expected) in self.data:
            actual = paid_staircase(n, p)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()