# Uses python3
import sys

def optimal_weight(W, w):
    dp = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for wt in range(1, W+1):
            dp[i][wt] = dp[i-1][wt]
            if w[i-1] <= wt:
                val = dp[i-1][wt - w[i-1]] + w[i-1]
                if dp[i][wt] < val:
                    dp[i][wt] = val

    return dp[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
