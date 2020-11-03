import unittest
from collections import Counter

# recursive
def fib(n):
    if n == 0: return 0
    if n <= 2: return 1

    return fib(n-1) + fib(n-2)

# top down -> recursion + memoization
def fib_top_down(n):
    memo = Counter()
    return fib_top_down_helper(n, memo)

def fib_top_down_helper(n, memo):
    if n == 0: return 0
    if n <= 2: return 1

    if memo[n] > 0:
        return memo[n]
    
    memo[n] = fib_top_down_helper(n-1, memo) + fib_top_down_helper(n-2, memo)
    return memo[n]

# bottom-up dynamic programming (forward dynamic programming)
#
# f(i-1)
#      \
#       >-------> f(i)
#      /
# f(i-2)
def fib_bottom_up_dp_forward(n):
    if n == 0: return 0
    if n <= 2: return 1

    dp = [None] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# this is a bottom-up dynamic programming (backward dynamic programming)
#
#   -----> f(i+2)
#   |
# f(i)
#   |
#   -----> f(i+1)
def fib_bottom_up_dp_backward(n):
    if n == 0: return 0
    if n <= 2: return 1

    dp = [0] * (n+2)
    dp[0] = 0
    dp[1] = 1

    for i in range(1, n):
        dp[i+1] += dp[i] # dp[i] is already solved; use it to solve other subproblems
        dp[i+2] += dp[i]
    return dp[n]

class Test(unittest.TestCase):
    '''Test Cases: (n, expected)'''
    data = [
        (0, 0),
        (1, 1),
        (2, 1),
        (10, 55),
    ] 

    def test_fib(self):
        for (n, expected) in self.data:
            actual = fib(n)
            self.assertEqual(actual, expected)

    def test_fib_top_down(self):
        for (n, expected) in self.data:
            actual = fib_top_down(n)
            self.assertEqual(actual, expected)

    def test_fib_bottom_up_dp_forward(self):
        for (n, expected) in self.data:
            actual = fib_bottom_up_dp_forward(n)
            self.assertEqual(actual, expected)

    def test_fib_bottom_up_dp_backward(self):
        for (n, expected) in self.data:
            actual = fib_bottom_up_dp_forward(n)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()