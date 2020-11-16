class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # ld -> last digit
        ld = num % 10
        if (ld == 2 
                or ld == 3 
                or ld == 7 
                or ld == 8):
            return False
        
        l = 1
        r = num
        while l <= r:
            mid = l + (r - l) // 2
            sq = mid ** 2
            if sq == num:
                return True
            elif sq < num:
                l = mid + 1
            else:
                r = mid - 1
                
        return False