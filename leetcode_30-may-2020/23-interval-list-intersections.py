from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        a_i = 0
        b_i = 0

        while a_i < len(A) and b_i < len(B):
            a_start, a_end = A[a_i]
            b_start, b_end = B[b_i]

            if a_end < b_start:
                a_i += 1
            elif b_end < a_start:
                b_i+= 1
            else:
                start = max(a_start, b_start)
                end = min(a_end, b_end)
                result.append([start, end])
                if a_end <= b_end:
                    a_i += 1
                elif a_end >= b_end:
                    b_i += 1

        return result