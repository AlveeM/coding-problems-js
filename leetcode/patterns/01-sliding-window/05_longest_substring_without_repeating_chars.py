# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# using dict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx = {}
        max_len = 0
        window_start = 0
        
        for window_end in range(len(s)):
            char = s[window_end]
            
            if char in char_idx:
                window_start = max(window_start, char_idx[char] + 1)
            
            char_idx[char] = window_end
            max_len = max(max_len, window_end - window_start + 1)
            
        return max_len

# using set
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        window_start = 0
        window_end = 0
        
        while window_end < len(s):
            char_start = s[window_start]
            char_end = s[window_end]
            
            if char_end not in seen:
                seen.add(char_end)
                max_len = max(max_len, window_end - window_start + 1)
                window_end += 1
            else:
                seen.remove(char_start)
                window_start += 1
            
        return max_len