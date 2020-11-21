class Solution:
    def longestCommonPrefix(self, strs):
        n = len(strs)

        # if strs is empty return ''
        if n == 0: return ''
        
        # initialize a variable to store common characters (res)
        res = []
        # initialize a variable and store the first string
        first_string = strs[0]
        
        # iterate through first string
        for i in range(len(first_string)):
            # initialize a variable and store the current character
            char = first_string[i]
            # iterate through rest of the strings
            for j in range(1, n):
                # if invalid index or character mismatch
                if i >= len(strs[j]) or strs[j][i] != char:
                    # return res as a string
                    return ''.join(res)
            # push the current character into res
            res.append(char)
            
        # return res as a string
        return ''.join(res)