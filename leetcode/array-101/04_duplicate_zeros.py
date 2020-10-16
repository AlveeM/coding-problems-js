from typing import List

# class Solution:
#     def duplicateZeros(self, arr):
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         result = []
#         for num in arr:
#             result.append(num)
#             if num == 0:
#                 result.append(num)

#         for i in range(len(arr)):
#             arr[i] = result[i]

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        arr_len = len(arr)

        for i in range(arr_len - 1, -1, -1):
            if  i + zeros < arr_len:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < arr_len:
                    arr[i + zeros] = arr[i]