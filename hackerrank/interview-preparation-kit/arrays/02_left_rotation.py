def rotLeft(a, d):
    n = len(a)
    res = [0] * n
    for i in range(n):
        res[(i - d % n)] = a[i]
    return res

arr = [1, 2, 3, 4, 5]
print(rotLeft(arr, 4)) # [5, 1, 2, 3, 4]