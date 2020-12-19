from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums, k):
        min_heap = []
        
        for i in range(k):
            heappush(min_heap, nums[i])
            
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])
        
        return min_heap[0]