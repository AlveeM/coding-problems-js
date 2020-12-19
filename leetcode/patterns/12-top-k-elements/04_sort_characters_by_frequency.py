from collections import Counter
from heapq import heappush, heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = Counter(s)
        max_heap = []
        res = []
        
        for char, freq in char_freq.items():
            heappush(max_heap, (-freq, char))
            
        while max_heap:
            item = heappop(max_heap)
            freq = -item[0]
            char = item[1]
            res.append(char * freq)
            
        return ''.join(res)