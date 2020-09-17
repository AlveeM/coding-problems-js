class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        count = [0]*26

        for char in s1:
            count[ord(char) - ord('a')] += 1
        start = 0
        for i in range(len(s1)):
            count[ord(s2[i]) - ord('a')] -= 1

        match = True
        for c in count:
            if c != 0:
                match = False
                break
        if match: return True
        start += 1

        while start <= len(s2) - len(s1):
            idx1 = ord(s2[start-1]) - ord('a')
            idx2 = ord(s2[start + len(s1) - 1]) - ord('a')
            count[idx1] += 1
            count[idx2] -= 1
            match = True
            for c in count:
                if c != 0:
                    match = False
                    break
            if match: return True
            start += 1

        return False