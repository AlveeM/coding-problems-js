from typing import List

# Iterative
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                result[j] = result[j] + result[j-1]
        
        return result

# Recursive
class Solution2:
    def __init__(self):
        self.cache = {}
        
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for colIndex in range(rowIndex + 1):
            result.append(self.getCellVal(rowIndex, colIndex))
        return result
    
    def getCellVal(self, rowIdx, colIdx):
        if colIdx == 0 or colIdx == rowIdx: return 1
        
        self.cache[(rowIdx-1, colIdx-1)] = self.cache.get((rowIdx-1, colIdx-1)) or self.getCellVal(rowIdx-1, colIdx-1)
        
        self.cache[(rowIdx-1, colIdx)] = self.cache.get((rowIdx-1, colIdx)) or self.getCellVal(rowIdx-1, colIdx)
        
        return self.cache[(rowIdx-1, colIdx-1)] + self.cache[(rowIdx-1, colIdx)]