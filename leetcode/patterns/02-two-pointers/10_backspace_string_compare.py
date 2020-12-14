class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i1 = len(S) - 1
        i2 = len(T) - 1
        
        while i1 >= 0 or i2 >= 0:
            i1 = self.nextIndex(S, i1)
            i2 = self.nextIndex(T, i2)
            if i1 < 0 and i2 < 0:
                return True
            if i1 < 0 or i2 < 0:
                return False
            if S[i1] != T[i2]:
                return False
            i1 -= 1
            i2 -= 1
        
        return True
        
    def nextIndex(self, string, idx):
        backspace_count = 0
        
        while idx >= 0:
            if string[idx] == '#':
                backspace_count += 1
            elif backspace_count > 0:
                backspace_count -= 1
            else:
                break
            idx -= 1
        
        return idx

