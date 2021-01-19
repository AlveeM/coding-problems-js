# https://youtu.be/FB0KUhsxXGY

class Solution:
  def minimumSubsetSum(self, nums):
    total = sum(nums)
    s = total // 2
    n = len(nums)
    dp = [[False] * (s+1) for _ in range(n)]

    for i in range(n):
      dp[i][0] = True

    for j in range(1, s+1):
      dp[0][j] = nums[0] == j

    for i in range(1, n):
      for j in range(1, s+1):
        if dp[i-1][j]:
          dp[i][j] = dp[i-1][j]
        elif j >= nums[i]:
          dp[i][j] = dp[i-1][j-nums[i]]

    for j in range(s, -1, -1):
      if dp[n-1][j]:
        # ans = abs(sum1 - sum2); sum1 = j; sum2 = total - j
        return abs(j - (total - j))
