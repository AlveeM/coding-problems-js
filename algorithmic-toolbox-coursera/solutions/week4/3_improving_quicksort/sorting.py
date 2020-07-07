# Uses python3
import sys
import random

def partition3(a, l, r):
    pivot_el = a[l]
    low_idx = l 
    high_idx = r
    p_idx = l

    while p_idx <= high_idx:
        if a[p_idx] < pivot_el:
            a[low_idx], a[p_idx] = a[p_idx], a[low_idx]
            low_idx += 1
        elif a[p_idx] > pivot_el:
            a[high_idx], a[p_idx] = a[p_idx], a[high_idx]
            high_idx -= 1
            p_idx -= 1
        p_idx += 1

    return low_idx, high_idx

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

# arr = [2, 3, 9, 2, 2]
# arr = [4, 1, 7, 3, 2, 8, 9]
# last_idx = len(arr)-1
# val = partition3(arr, 0, last_idx)
# print(val)
# randomized_quick_sort(arr, 0, last_idx)
# print(arr)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
