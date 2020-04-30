/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function (text1, text2) {
  // var: 2D grid to store longest common subsequence result
  let grid = new Array(text1.length+1).fill(0)
              .map(()=> new Array(text2.length+1).fill(0));

  // traverse grid diagonally
  for (let i=1; i < grid.length; i++) {
    for (let j=1; j < grid[0].length; j++) {
      // if: same chars at index: add 1 to previous diag and store in current diag
      if (text1[i-1] == text2[j-1]) {
        grid[i][j] = grid[i-1][j-1] + 1;
      // else: store the max between top and left cells
      } else {
        grid[i][j] = Math.max(grid[i][j-1], grid[i-1][j]);
      }
    }
  }

  // return last element in grid
  return grid[grid.length - 1][grid[0].length - 1];
};