class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        prev = 0
        cur = 0
        total = 0
        
        for char in s[::-1]:
            cur = mapping[char]
            if prev > cur:
                total -= cur
            else:
                total += cur
            prev = cur
            
        return total
            