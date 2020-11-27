# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        max_freq = 0
        window_start = 0
        
        for window_end in range(len(s)):
            char_end = s[window_end]
            
            char_freq[char_end] += 1
            max_freq = max(max_freq, char_freq[char_end])
            
            window_size = window_end - window_start + 1
            if window_size - max_freq > k:
                char_start = s[window_start]
                char_freq[char_start] -= 1
                window_start += 1
            
        return len(s) - window_start

from collections import defaultdict

class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        max_freq = 0
        window_start = 0
        
        for window_end in range(len(s)):
            char_end = s[window_end]
            
            char_freq[char_end] += 1
            max_freq = max(max_freq, char_freq[char_end])
            
            window_size = window_end - window_start + 1
            if window_size - max_freq > k:
                char_start = s[window_start]
                char_freq[char_start] -= 1
                window_start += 1
            
        return len(s) - window_start