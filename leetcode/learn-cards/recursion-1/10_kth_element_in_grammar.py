class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K == 1: return 0

        half_len = 2**(N-1) / 2
        if K <= half_len:
            return self.kthGrammar(N-1, K)
        else:
            res = self.kthGrammar(N-1, K-half_len)
            # if res == 1: return 0
            # return 1
            return int(not(res))