# Uses python3
import sys

# Coins available: 1, 5, 10
def get_change(m):
    coin_count = 0

    while (m - 10 >= 0):
        m -= 10
        coin_count += 1

    while (m - 5 >= 0):
        m -= 5
        coin_count += 1

    while (m - 1 >= 0):
        m -= 1
        coin_count += 1

    return coin_count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
