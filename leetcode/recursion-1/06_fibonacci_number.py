class Solution1:
    def fib(self, N: int) -> int:
        if N < 2: return N
        return self.fib(N - 1) + self.fib(N - 2)

class Solution2:
    def fib(self, N: int) -> int:
        cache = {
            0: 0,
            1: 1,
            2: 1,
        }
        
        def helper(n):
            if n in cache:
                return cache[n]
            
            res = helper(n-1) + helper(n-2)
            cache[n] = res
            return res
            
        return helper(N)

class Solution3:
    def fib(self, N: int) -> int:
        cache = [0, 1, 1]
        
        if N <= 2:
            return cache[N]
        
        for i in range(3, N+1):
            cache.append(cache[i-1] + cache[i-2])
            
        return cache[N]

class Solution4:
    def fib(self, N: int) -> int:
        if N <= 1: return N
        
        prev = 0
        cur = 1
        for _ in range(N-1):
            temp = cur
            cur = cur + prev
            prev = temp
            
        return cur