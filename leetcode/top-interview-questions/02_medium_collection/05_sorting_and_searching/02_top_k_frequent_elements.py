from heapq import *
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq_map = Counter(nums)
        min_heap = []

        for num, freq in num_freq_map.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)
        
        top_nums = []
        while min_heap:
            top_nums.append(heappop(min_heap)[1])
        
        return top_nums