class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        l, r = 0, 0 # start and end index of current longest substring
        dp = [[False] * n for _ in range(n)]
        
        # set all 1 letter strings to True
        for i in range(n):
            dp[i][i] = True
            
        # set 2 letter palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if l == 0 and r == 0:
                    l, r = i, i + 1

        # set 3+ letter palindromes
        for i in range(2, n):
            for j in range(n - 2):
                k = i + j
                # dp matrix boundary check
                if k == n:
                    break
                # check if substring is palindrome
                # cond 1: first and last letter is same
                # cond 2: substring (dp[j + 1][k - 1]) is a palindrome
                if s[j] == s[k] and dp[j + 1][k - 1]:
                    dp[j][k] = True
                    # set longest substring
                    # length of substring(j, k) > length of substring(l, r)
                    if k - j > r - l:
                        l, r = j, k
        
        return s[l:r + 1]