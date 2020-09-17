class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        invalid_last_digits = {2, 3, 7, 8}
        last_digit = num % 10

        if (last_digit in invalid_last_digits) or num == 0:
            return False

        left = 1
        right = num
        while left <= right:
            mid = left + (right - left) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False