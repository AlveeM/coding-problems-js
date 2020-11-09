from heapq import heappush, heappop

class Solution:
    def findClosestElements(self, arr, k, x):
        x_idx = self.binarySearch(arr, x)
        low = max(x_idx - k, 0)
        high = min(x_idx + k, len(arr) - 1)
        minheap = []
        
        for i in range(low, high+1):
            heappush(minheap, (abs(arr[i] - x), arr[i]))
            
        result = []
        for _ in range(k):
            result.append(heappop(minheap)[1])
            
        result.sort()
        return result
        
        
    def binarySearch(self, arr, x):
        l = 0
        r = len(arr) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
                
        return l


