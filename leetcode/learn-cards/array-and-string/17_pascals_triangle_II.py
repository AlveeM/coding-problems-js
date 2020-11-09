class Solution:
    def getRow(self, rowIndex):
        prev = [1]
        cur = [1]
        
        for size in range(2, rowIndex + 2):
            cur = [1] * size
            for i in range(1, size-1):
                cur[i] = prev[i-1] + prev[i]
            prev = cur
                
        return cur