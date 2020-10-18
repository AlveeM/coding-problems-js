# def sum_array(arr):
#     if len(arr) == 1:
#         return arr[0]

#     return arr[0] + sum_array(arr[1:])

def sum_array(arr, idx=0):
    if len(arr) == 0:
        return arr

    if idx == len(arr)-1:
        return arr[idx]

    return arr[idx] + sum_array(arr, idx + 1)

arr = [1, 2, 3, 4, 5, 6]
arr = []
print(sum_array(arr))