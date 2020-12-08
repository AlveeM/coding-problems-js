class Solution:
    def letterCasePermutation(self, S):
        res = [S]
        for i in range(len(S)):
            if S[i].isalpha():
                n = len(res)
                for j in range(n):
                    string = res[j]
                    res.append(string[:i] + string[i].swapcase() + string[i+1:])
        return res