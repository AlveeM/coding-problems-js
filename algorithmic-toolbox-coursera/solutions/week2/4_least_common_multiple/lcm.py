# Uses python3
import sys

def gcd_euclid(a, b):
    if b == 0:
        return a

    a_bar = a % b
    return gcd_euclid(b, a_bar)

def lcm_naive(a, b):
    gcd = gcd_euclid(a, b)
    return (a * b) // gcd

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
