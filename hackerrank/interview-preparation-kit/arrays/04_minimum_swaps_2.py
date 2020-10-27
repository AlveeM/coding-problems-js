# def minimumSwaps(arr):
#     visited_dict = {}
#     count = 0
#     for i in range(len(arr)):
#         if i not in visited_dict:
#             j = arr[i] - 1
#             while i not in visited_dict:
#                 count += 1
#                 visited_dict[j] = True
#                 j = arr[j] - 1
#             count -= 1
#     return count

def minimumSwaps(arr):
    visited_dict = {}
    count = 0
    for i in range(len(arr)):
        if i not in visited_dict:
            j = arr[i] - 1
            while i != j:
                visited_dict[j] = True
                j = arr[j] - 1
                count += 1
    return count