from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
                
        return anagrams.values()

class Solution2:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        return anagrams.values()