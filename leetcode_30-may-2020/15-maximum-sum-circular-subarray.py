from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total_sum = 0
        max_end_at = 0
        min_end_at = 0
        max_sum = -float('inf')
        min_sum = float('inf')

        for num in A:
            total_sum += num
            max_end_at = max(max_end_at + num, num)
            max_sum = max(max_end_at, max_sum)
            min_end_at = min(min_end_at + num, num)
            min_sum = min(min_end_at, min_sum)

        if total_sum == min_sum:
            return max_sum

        return max(max_sum, total_sum - min_sum)
