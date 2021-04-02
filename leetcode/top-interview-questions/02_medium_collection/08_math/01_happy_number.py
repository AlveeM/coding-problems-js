class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.findSquare(n)
        
        return n == 1
        
    def findSquare(self, n: int) -> int:
        square = 0
        
        while n != 0:
            square += (n % 10) ** 2
            n = n // 10
        
        return square