/**
 * @param {character[][]} grid
 * @return {number}
 */
function numIslands(grid) {
  // edge: no grid
  if (grid == null || grid.length == 0) return 0;

  // var: island count tracker
  let numIs = 0;

  // iterate through each grid element
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      // if: el is '1'; update numIs by traversing grid
      if (grid[i][j] == '1') {
        numIs += DFS(grid, i, j);
      }
    }
  }

  // return result
  return numIs;
};

function DFS(grid, i, j) {
  // base cases
  if (i < 0
    || i >= grid.length
    || j < 0
    || j >= grid[i].length
    || grid[i][j] == '0'
  ) {
    return 0;
  }

  // mark current grid element as done
  grid[i][j] = 0;

  // traversal
  DFS(grid, i + 1, j);
  DFS(grid, i - 1, j);
  DFS(grid, i, j + 1);
  DFS(grid, i, j - 1);

  // return 1
  return 1;
}

let grid = [
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
];

console.log(numIslands(grid));