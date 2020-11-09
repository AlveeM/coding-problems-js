class Solution:
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0: return ''
        
        prefix = []
        for i, char in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return ''.join(prefix)
            prefix.append(char)
                
        return ''.join(prefix)

class Solution2:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''
        
        prefix = []
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix.append(chars[0])
            else:
                return ''.join(prefix)
            
        return ''.join(prefix)