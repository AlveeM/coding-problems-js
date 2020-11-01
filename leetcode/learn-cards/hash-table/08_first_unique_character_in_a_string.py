from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = Counter(s)
        
        for idx, char in enumerate(s):
            if char_counts[char] == 1:
                return idx
            
        return -1