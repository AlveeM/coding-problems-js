# https://youtu.be/MqYLmIzl8sQ

class Solution:
  def countSubsetsWithSum(self, nums, target):
    n = len(nums)
    dp = [[None] * (target + 1) for _ in range(n+1)]

    for i in range(n+1):
      dp[i][0] = 1

    for j in range(1, target+1):
      dp[0][j] = 0

    for i in range(1, n+1):
      for j in range(1, target+1):
        if nums[i-1] > j:
          dp[i][j] = dp[i-1][j]
        elif nums[i-1] <= j:
          dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]

    return dp[n][target]
