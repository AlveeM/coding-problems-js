class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        
        while True:
            slow = self.findSquare(slow)
            fast = self.findSquare(self.findSquare(fast))
            if slow == fast:
                break

        return slow == 1
        
    def findSquare(self, n):
        square = 0
        while n != 0:
            square += (n % 10) ** 2
            n = n // 10
        return square
    
class Solution2:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.find_square(n)
            
        return n == 1
        
    def find_square(self, num: int) -> int:
        square = 0

        while num != 0:
            square += (num % 10) ** 2
            num = num // 10

        return square