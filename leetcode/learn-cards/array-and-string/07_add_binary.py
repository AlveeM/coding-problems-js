class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0:
            total = carry
            
            if i >= 0: total += ord(a[i]) - ord('0')
            if j >= 0: total += ord(b[j]) - ord('0')
            carry = total // 2
            result.append(str(total % 2))
            
            i, j = i - 1, j - 1
        
        if carry != 0: result.append(str(carry))
        return ''.join(result[::-1])