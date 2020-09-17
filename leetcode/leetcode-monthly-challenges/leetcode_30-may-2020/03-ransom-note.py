from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(ransomNote)
        for key,val in count.items():
            if magazine.count(key) < val:
                return False

        return True