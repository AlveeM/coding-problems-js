from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        s_counts = Counter(s)
        for char in t:
            if s_counts[char] <= 0:
                return False
            s_counts[char] -= 1
            
        return True