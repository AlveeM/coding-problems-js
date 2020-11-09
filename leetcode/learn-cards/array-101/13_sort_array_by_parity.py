class Solution:
    def sortArrayByParity(self, A):
        e = 0
        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[e], A[i] = A[i], A[e]
                e += 1
                
        return A