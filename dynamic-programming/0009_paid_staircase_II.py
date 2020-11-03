import unittest

'''
Problem: Paid Staircase II
	You are climbing a paid staircase. It takes n steps to reach to the top and you have to
	pay p[i] to step on the i-th stair. Each time you can climb 1 or 2 steps.
	Return the cheapest path to the top of the staircase.

Template to reconstruct the path
	path = []
	for curr = best_last_state; curr exists; curr = from[curr] {
		path.push(curr)
	}
	return path.reverse()
''' 

def paid_staircase(n, p):
    dp = [0] * (n+1)
    track = [0] * (n+1)

    dp[0] = 0
    dp[1] = p[1]

    for i in range(2, n+1):
        dp[i] = min(dp[i-1], dp[i-2]) + p[i]

        if dp[i-1] < dp[i-2]:
            track[i] = i-1
        else:
            track[i] = i-2

    path = []
    cur = n
    while cur > 0:
        path.append(cur)
        cur = track[cur]
    path.append(cur)

    return list(reversed(path))

class Test(unittest.TestCase):
    '''Test Cases: (n, p, expected)'''
    data = [
        (8, [0, 3, 2, 4, 6, 1, 1, 5, 3], [0, 2, 3, 5, 6, 8]),
    ]

    def test_paid_staircase(self):
        for (n, p, expected) in self.data:
            actual = paid_staircase(n, p)
            self.assertEqual(actual, expected)
            
if __name__ == "__main__":
    unittest.main()