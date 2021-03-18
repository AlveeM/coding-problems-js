class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}
        max_len = 0
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            
            if char in char_idx:
                l = max(l, char_idx[char] + 1)
            
            char_idx[char] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        seen = {}
        l = max_len = 0
        
        for r,val in enumerate(s):
            if val in seen and l <= seen[val]:
                l = seen[val] + 1
            else:
                max_len = max(max_len, r - l + 1)
            
            seen[val] = r
        
        return max_len
        