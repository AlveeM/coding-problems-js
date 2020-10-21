class Solution1:
    def climbStairs(self, n: int) -> int:
        def fib(N):
            if N <= 1: return N
            
            prev = 0
            cur = 1
            for _ in range(N-1):
                temp = cur
                cur =  cur + prev
                prev = temp
                
            return cur
        
        return fib(n + 1)

class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
            
        prev = 1
        cur = 1
        for _ in range(n-1):
            temp = cur
            cur =  cur + prev
            prev = temp

        return cur
        