class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char in columnTitle:
            diff = ord(char) - ord('A') + 1
            res = res * 26 + diff
        return res