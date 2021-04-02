class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.powRec(x, -n)
        return self.powRec(x, n)
    
    def powRec(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            return self.powRec(x * x, n / 2)
        else:
            return x * self.powRec(x, n - 1)

class Solution2:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1
        while n:
            if n % 2 != 0:
                res *= x
            x *= x
            n //= 2
        return res