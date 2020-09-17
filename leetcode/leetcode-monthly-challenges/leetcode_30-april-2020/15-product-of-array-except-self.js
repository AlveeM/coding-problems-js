/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  // var: result array; init all elements to first el of nums
  let result = Array(nums.length).fill(nums[0]);
  // var: temp; init to last el of nums
  let temp = nums[nums.length - 1];
  // iterate over result arr; 2nd -> end
  for (let i = 1; i < result.length; i++) {
    // update curr el: result el at prev idx * nums el at curr idx
    result[i] = result[i-1] * nums[i];
  }
  // update last el of result to second to last el
  result[result.length - 1] = result[result.length - 2];
  // iterate over result; 2nd to last -> 2nd element
  for (let i = result.length - 2; i > 0; i--) {
    // update curr el: product of prev el and temp
    result[i] = result[i - 1] * temp;
    // update temp: temp * el of nums at current idx
    temp = temp * nums[i];
  }
  // update first el of result to temp
  result[0] = temp;
  // return result
  return result;
};