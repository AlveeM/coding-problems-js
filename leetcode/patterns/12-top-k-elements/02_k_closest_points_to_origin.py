from heapq import heappush, heapreplace

class Solution:
    def kClosest(self, points, K):
        max_heap = []
        for i in range(K):
            heappush(max_heap, (-self.distance(points[i]),  points[i]))
        
        for i in range(K, len(points)):
            distance, _ = max_heap[0]
            if -distance > self.distance(points[i]):
                heapreplace(max_heap, (-self.distance(points[i]), points[i]))
                
        return [items[1] for items in max_heap]
        
    def distance(self, point):
        return (point[0] ** 2) + (point[1] ** 2)