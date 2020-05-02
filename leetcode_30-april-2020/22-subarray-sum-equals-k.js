/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
  // edge: empty array
  if (nums.length == 0) return 0;

  // var: count; track number of subarrays that sum to k
  let count = 0;
  // var: prefix sum hash; key: prefix sum, value: count of prefix sum
  let psHash = {};
  // var: current sum; store sum up to current index; initialize to 0
  let curSum = 0;

  // iterate over nums
  for (let num of nums) {
    // increment curSum by current element
    curSum += num;
    // if: curSum == k; increment count
    if (curSum == k) count++;
    // if: (curSum - K) in hash; increment count by prefix sum count
    if ((curSum - k) in psHash) count += psHash[curSum - k];
    // if: prefix sum in hash; increment
    if (curSum in psHash){
      psHash[curSum]++;
      // else: initialize to 1
    } else {
      psHash[curSum] = 1;
    }
  }

  // return count
  return count;
};

console.log(subarraySum([1,1,1], 2)); // 2