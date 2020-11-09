class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        
        result = []
        while i < n:
            while i < n and s[i] == ' ': i += 1
            
            j = i + 1
            while j < n and s[j] != ' ': j += 1
            
            substr = s[i:j]
            if substr:
                result.append(substr)
                    
            i = j + 1
            
        return ' '.join(reversed(result))