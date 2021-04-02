class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        
        while l <= r:
            mid = (l + r) // 2
            
            x_temp = mid * mid
            if x_temp == x:
                return mid
            elif x_temp > x:
                r = mid - 1
            else:
                l = mid + 1
        
        return r