class Solution:        
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        maxsize = 2**31
        minsize = -(2**31) - 1
        x = abs(x)
        res = 0
        
        while x > 0:
            res = (res * 10) + (x % 10)
            x = x // 10
            
        res = sign * res
        if minsize < res < maxsize:
            return res
        else:
            return 0