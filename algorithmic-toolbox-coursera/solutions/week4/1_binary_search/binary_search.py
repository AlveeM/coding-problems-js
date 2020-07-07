# Uses python3
import sys

def binary_search(a, x):
    start_idx = 0
    end_idx = len(a) - 1

    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        mid_el = a[mid_idx]

        if x == mid_el:
            return mid_idx
        elif x < mid_el:
            end_idx = mid_idx - 1
        else:
            start_idx = mid_idx + 1

    return -1

# def linear_search(a, x):
#     for i in range(len(a)):
#         if a[i] == x:
#             return i
#     return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
