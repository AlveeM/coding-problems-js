from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         count = [0] * 26

#         for char in s:
#             count[ord(char) - ord('a')] += 1

#         for i in range(len(s)):
#             if (count[ord(s[i]) - ord('a')] == 1):
#                 return i

#         return -1