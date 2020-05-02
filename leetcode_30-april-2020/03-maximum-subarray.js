/**
 * @param {number[]} nums
 * @return {number}
 */
function maxSubArray(nums) {
  let currMax = nums[0]
  let globalMax = nums[0]
  for (let i = 1; i < nums.length; i++) {
    if (currMax < 0) {
      currMax = nums[i]
    } else {
      currMax += nums[i]
    }

    globalMax = Math.max(globalMax, currMax);
  }
  return globalMax
}