class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        l = 0
        r = 0
        result = []
        
        while l < n:
            while r < n and s[r] != ' ': r += 1
            
            substr = s[l:r]
            result.append(substr[::-1])
            
            l = r + 1
            r = l
            
        return ' '.join(result)

class Solution2:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split()])