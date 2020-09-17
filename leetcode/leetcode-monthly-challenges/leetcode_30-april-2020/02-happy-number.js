/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n, counter = 0) {
  if (counter > 9) {
    return false;
  }

  if (n == 1) {
    return true;
  }

  n = splitAndSum(n);
  return isHappy(n, ++counter);
};

var splitAndSum = function (n) {
  let nums = [];
  while (n > 0) {
    nums.unshift(n % 10);
    n = parseInt(n / 10);
  }
  return nums.reduce((a, b) => a + b ** 2, 0);
}