class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        count = 0
        m = len(grid)
        n = len(grid[0])
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    self.markGrid(grid, r, c)
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