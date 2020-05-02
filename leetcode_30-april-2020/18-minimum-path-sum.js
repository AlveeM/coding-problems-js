/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function (grid) {
  debugger;
  // edge: empty grid
  if (grid.length == 0) return 0;

  // var: store row length
  let rowLen = grid.length;
  // var: store col length
  let colLen = grid[0].length;

  // iterate over first row
  for (let col = 1; col < colLen; col++) {
    // update grid: current el + prev el
    grid[0][col] += grid[0][col-1];
  }

  // iterate over remaining elements
  for (let row = 1; row < rowLen; row++) {
    // update 1st col: current el + top el
    grid[row][0] += grid[row-1][0];
    // iterate over and update remaining cols
    for (let col = 1; col < colLen; col++) {
      grid[row][col] += Math.min(
        grid[row-1][col],
        grid[row][col-1]
      );
    }
  }

  return grid[rowLen-1][colLen-1];
};

let grid = [[1,3,1],
            [1,5,1],
            [4,2,1]];
console.log(minPathSum(grid));