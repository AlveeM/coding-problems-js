import unittest

'''
Problem: Find the sum of the first N numbers.

Objective function:
f(i) is the sum of the first i elements.

Recurrence relation:
f(n) = f(n-1) + n
'''

def sum_of_nums(n):
    dp = [0] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        dp[i] = dp[i-1] + i
    return dp[n]

class Test(unittest.TestCase):
    '''Test Cases: (n, expected)'''
    data = [
        (0, 0),
        (1, 1),
        (5, 15),
    ]

    def test_sum_of_nums(self):
        for (n, expected) in self.data:
            actual = sum_of_nums(n)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()