# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

def maxSubArrayOfSizeK(k, arr):
  if len(arr) < k: return 0
  
  max_sum = 0
  for i in range(k):
    max_sum += arr[i]

  window_sum = max_sum
  for window_end in range(k, len(arr)):
    window_start = window_end - k
    window_sum = window_sum - arr[window_start] + arr[window_end]
    max_sum = max(window_sum, max_sum)

  return max_sum
