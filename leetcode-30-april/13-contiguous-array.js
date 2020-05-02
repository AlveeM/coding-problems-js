/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function (nums) {
  let maxLen = 0;
  let hash = new Map();
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      count -= 1
    } else {
      count += 1
    }
    if (count === 0)
      maxLen = i + 1;
    if (hash.has(count)) {
      maxLen = Math.max(maxLen, i - hash.get(count))
    } else {
      hash.set(count, i);
    }
  }
  return maxLen;
};

console.log(findMaxLength([0, 1, 0, 1]));