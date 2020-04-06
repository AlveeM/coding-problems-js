/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  // declare variable to keep track of min price, initialized to first stock
  let min = prices[0];
  // declare variable to keep track of profit
  let profit = 0;
  // iterate over the prices from 2nd element
  for (let i = 1; i < prices.length; i++) {
    // if current stock < min price, replace min
    if (prices[i] < min) {
      min = prices[i];
    }
    // if current stock > min price
    if (prices[i] > min) {
      // if last stock in array, update profit
      if ((i + 1) == prices.length) {
        profit += prices[i] - min;
        // else if next stock < current stock, update profit and min
      } else if (prices[i + 1] < prices[i]) {
        profit += prices[i] - min;
        min = prices[i + 1];
      }
    }
  }
  return profit;
};