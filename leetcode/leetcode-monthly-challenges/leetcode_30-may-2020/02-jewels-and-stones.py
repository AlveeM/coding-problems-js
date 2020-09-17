class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        jewel_set = set(J)
        for char in S:
            if char in jewel_set:
                count += 1

        return count