class Solution:
  def threeSumSmaller(self, nums, target):
    nums.sort()
    count = 0

    for i in range(len(nums)-2):
      l = i + 1
      r = len(nums) - 1

      while l < r:
        cur_sum = nums[i] + nums[l] + nums[r]
        if cur_sum >= target:
          r -= 1
        else:
          count += r - l
          l += 1

    return count
