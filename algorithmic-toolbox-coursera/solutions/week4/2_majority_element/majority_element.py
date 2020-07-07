# Uses python3
import sys

def get_majority_element(a, left, right):
    idx = 0
    count = 1

    for i in range(1, len(a)):
        if a[i] == a[idx]:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            idx = i
            count = 1
    
    count = 0
    for el in a:
        if el == a[idx]:
            count += 1

    if count > (len(a) // 2):
        return a[idx]
    else:
        return -1

# arr = [1, 2, 3, 1]
# arr = [2, 3, 9, 2, 2]
# arr = [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]
# print(get_majority_element(arr, 0, len(arr)))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
