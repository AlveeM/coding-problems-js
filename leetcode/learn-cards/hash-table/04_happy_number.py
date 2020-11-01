class Solution:
    def isHappy(self, n):
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.find_square(n)
            
        return n == 1
        
    def find_square(self, num):
        square = 0

        while num != 0:
            square += (num % 10) ** 2
            num = num // 10

        return square


Solution().isHappy(19) # happy :) 
Solution().isHappy(25) # not happy :(