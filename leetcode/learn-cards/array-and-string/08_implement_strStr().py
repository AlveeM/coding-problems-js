class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0
        
        h_len = len(haystack)
        n_len = len(needle)
        
        for i in range(h_len - n_len + 1):
            for j in range(n_len):
                if haystack[i+j] != needle[j]:
                    break
                if j == n_len-1:
                    return i
                
        return -1