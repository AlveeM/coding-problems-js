from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if (1000 <= num <= 9999) or (10 <= num <= 99) or num == 100000:
                count += 1
                
        return count