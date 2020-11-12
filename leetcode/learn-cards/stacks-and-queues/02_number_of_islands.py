# Method 1: DFS
class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        count = 0
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.markGrid(grid, i, j)
                    count += 1
        
        return count
    
    def markGrid(self, grid, r, c):
        grid[r][c] = '2'
        m = len(grid)
        n = len(grid[0])
        
        if r - 1 >= 0 and grid[r-1][c] == '1':
            self.markGrid(grid, r-1, c)
        if r + 1 < m and grid[r+1][c] == '1':
            self.markGrid(grid, r+1, c)
        if c - 1 >= 0 and grid[r][c-1] == '1':
            self.markGrid(grid, r, c-1)
        if c + 1 < n and grid[r][c+1] == '1':
            self.markGrid(grid, r, c+1)

# Method 2: BFS
from collections import deque
class Solution2:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.markGrid(grid, i, j)
                    count += 1
        
        return count
    
    def markGrid(self, grid, r, c):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '2'
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while queue:
            r, c = queue.popleft()
            for r_shift, c_shift in directions:
                nr, nc = r + r_shift, c + c_shift
                if self.is_within_bounds(grid, nr, nc) and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '2'
    
    def is_within_bounds(self, grid, r, c):
        m = len(grid)
        n = len(grid[0])
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        else:
            return True
        