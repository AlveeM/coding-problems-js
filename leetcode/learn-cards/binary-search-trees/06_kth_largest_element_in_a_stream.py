from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapify(self.nums)
        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val):
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]