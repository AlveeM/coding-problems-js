from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums, k):
        res = []
        max_heap = []
        nums_freq = Counter(nums)
        
        for num, freq in nums_freq.items():
            heappush(max_heap, (-freq, num))
            
        for _ in range(k):
            freq, num = heappop(max_heap)
            res.append(num)
            
        return res