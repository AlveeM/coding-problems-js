/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  // var: track max_reach of current element
  let maxReach = 0;
  // iterate over nums
  for (let i = 0; i < nums.length; i++){
    // if: current index jump > maxReach; update maxReach
    if (nums[i] + i > maxReach) {
      maxReach = nums[i] + i
    }
    // if: maxReach == i; break
    if (maxReach == i) break;
  }
  // return true if maxReach >= last index
  return maxReach >= nums.length - 1
};