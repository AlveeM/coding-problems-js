from typing import List

# T: O(n^2) [since input can be n(n-1) / 2]
# S: O(n)
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_count = [0]*N
        result = -1

        for pair in trust:
            trust_count[pair[0]-1] -= 1
            trust_count[pair[1]-1] += 1

        for idx in range(N):
            if trust_count[idx] == N-1:
                return idx + 1

        return result
