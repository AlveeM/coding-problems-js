from math import sqrt
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(sqrt(n) + 1))]
        depth = 1
        q = deque([n])
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for sq in squares:
                    if cur == sq: return depth
                    if cur < sq: break
                    q.append(cur-sq)
            
            depth += 1
            
        return 0