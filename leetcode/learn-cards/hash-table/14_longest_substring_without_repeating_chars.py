class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        char_idx_dict = {}
        max_len = 0
        
        for window_end in range(len(s)):
            cur_char = s[window_end]
            
            if cur_char in char_idx_dict:
                window_start = max(window_start, char_idx_dict[cur_char] + 1)
            
            char_idx_dict[cur_char] = window_end
            max_len = max(max_len, window_end - window_start + 1)
            
        return max_len