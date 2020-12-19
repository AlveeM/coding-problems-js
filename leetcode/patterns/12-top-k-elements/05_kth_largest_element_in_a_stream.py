import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]