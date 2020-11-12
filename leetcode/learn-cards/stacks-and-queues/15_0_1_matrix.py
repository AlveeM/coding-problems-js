from collections import deque

class Solution:
    def updateMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        def bfs(r, c):
            q = deque()
            q.append(((r, c), 0))
            visited = set()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while q:
                for _ in range(len(q)):
                    coord, d = q.popleft()
                    rq, cq = coord
                    
                    if matrix[rq][cq] == 0:
                        return d
                    
                    visited.add((rq, cq))
                    for r_shift, c_shift in directions:
                        nr = rq + r_shift
                        nc = cq + c_shift
                        if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                            q.append(((nr, nc), d+1))
          
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    matrix[r][c] = bfs(r, c)
        
        return matrix
