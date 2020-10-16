from typing import List

# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         cur_max = -1

#         for i in range(len(arr)-1, -1, -1):
#             cur_el = arr[i]
#             arr[i] = cur_max
#             cur_max = max(cur_max, cur_el)
            
#         return arr

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = cur_max
            if temp > cur_max:
                cur_max = temp

        return arr