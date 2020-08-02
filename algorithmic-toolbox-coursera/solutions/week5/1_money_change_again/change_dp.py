# Uses python3
import sys

def get_change(m, coins=[1, 3, 4]):
    min_coins = [0 for _ in range(m+1)]
    for i in range(1, m+1):
        min_coins[i] = float('inf')
        for coin in coins:
            if i >= coin:
                num_coins = min_coins[i - coin] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins

    return min_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
