class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        maxPowerOfThree = 1162261467
        return n > 0 and maxPowerOfThree % n == 0