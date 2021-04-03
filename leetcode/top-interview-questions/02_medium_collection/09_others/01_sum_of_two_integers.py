class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # 32 bits
        while(b != 0):
            s = (a ^ b) & mask
            c = ((a & b) << 1) & mask
            a = s & mask
            b = c & mask
        
        max_int = 0x7FFFFFFF
        
        if a < max_int:
            return a 
        else:
            return ~(a ^ mask)