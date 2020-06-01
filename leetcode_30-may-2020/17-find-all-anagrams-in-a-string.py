from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result

        pchars = [0] * 26

        for char in p:
            pchars[ord(char) - ord('a')] += 1

        start = 0
        for i in range(len(p)):
            pchars[ord(s[i]) - ord('a')] -= 1

        mismatch = 0
        for char in pchars:
            if char != 0:
                mismatch += 1
        if mismatch == 0:
            result.append(start)
        start += 1

        while start <= (len(s) - len(p)):
            idx1 = ord(s[start - 1]) - ord('a')
            idx2 = ord(s[start + len(p)-1]) - ord('a')

            pchars[idx1] += 1
            if pchars[idx1] == 1:
                mismatch += 1
            elif pchars[idx1] == 0:
                mismatch -= 1

            pchars[idx2] -= 1
            if pchars[idx2] == -1:
                mismatch += 1
            elif pchars[idx2] == 0:
                mismatch -= 1

            if mismatch == 0:
                result.append(start)
            start += 1

        return result