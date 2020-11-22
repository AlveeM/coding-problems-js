class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        
        res = []
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return ''.join(res)
            res.append(char)
            
        return ''.join(res)