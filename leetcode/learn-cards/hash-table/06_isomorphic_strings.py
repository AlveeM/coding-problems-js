class Solution:
    def isIsomorphic(self, s, t):
        s_t = {}
        t_s = {}
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            if s_char in s_t and s_t[s_char] != t_char:
                return False
            if t_char in t_s and t_s[t_char] != s_char:
                return False
            
            s_t[s_char] = t_char
            t_s[t_char] = s_char
            
        return True