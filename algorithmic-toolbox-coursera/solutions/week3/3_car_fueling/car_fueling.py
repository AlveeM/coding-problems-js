# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refills = 0
    current_refill = 0
    n = len(stops)
    stops = [0] + stops + [distance]

    while current_refill <= n:
        last_refil = current_refill
        while ((current_refill <= n) and 
               (stops[current_refill + 1] - stops[last_refil] <= tank)):
            current_refill += 1
        if current_refill == last_refil:
            return -1
        if current_refill <= n:
            num_refills += 1

    return num_refills

# distance = 950
# tank = 400
# n = 4
# stops = [200, 375, 550, 750]
# distance = 10
# tank = 3
# n = 4
# stops = [1, 2, 5, 9]
# result = compute_min_refills(distance, tank, stops)
# print(result)

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
