/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  // var: start index
  let start = 0;
  // var: last index
  let end = nums.length - 1;

  // edge: start > end
  if (start > end) return -1;

  //loop until start <= end
  while (start <= end) {
    // var: mid point
    let mid = start + Math.floor((end - start) / 2);

    // case 0: mid == target
    if (nums[mid] == target) return mid;

    // case 1: target is between start and mid
    if (
      nums[start] <= nums[mid]
      && target <= nums[mid]
      && target >= nums[start]
    ) {
      end = mid - 1;
      // case 2: target is between mid and end
    } else if (
      nums[mid] <= nums[end]
      && target >= nums[mid]
      && target <= nums[end]
    ) {
      start = mid + 1;
      // case 3: end is < mid
    } else if (nums[end] <= nums[mid]) {
      start = mid + 1;
    } else if (nums[start] >= nums[mid]) {
      // case 4: start > mid
      end = mid - 1;
    } else if (end >= mid) {
      return -1;
    }
  }

  return -1;
};

console.log(search([4,5,6,7,0,1,2], 0));
console.log(search([4,5,6,7,0,1,2], 3));
console.log(search([1], 0));
console.log(search([1], 1));