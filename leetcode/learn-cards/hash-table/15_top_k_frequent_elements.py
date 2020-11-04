from heapq import heappush, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        if k == len(nums): return nums
        
        result = []
        heap = []
        nums_freq = Counter(nums)
        
        for num, freq in nums_freq.items():
            heappush(heap, (-1 * freq, num))
        
        for _ in range(k):
            freq, num = heappop(heap)
            result.append(num)
            
        return result