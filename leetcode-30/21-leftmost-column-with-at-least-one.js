/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * function BinaryMatrix() {
 *     @param {integer} x, y
 *     @return {integer}
 *     this.get = function(x, y) {
 *         ...
 *     };
 *
 *     @return {[integer, integer]}
 *     this.dimensions = function() {
 *         ...
 *     };
 * };
 */

/**
 * @param {BinaryMatrix} binaryMatrix
 * @return {number}
 */
var leftMostColumnWithOne = function (binaryMatrix) {
  // var: store binaryMatrix dimension
  let dim = binaryMatrix.dimensions()
  // var: no. of rows
  let rows = dim[0];
  // var: no. of cols
  let cols = dim[1];

  // edge: empty
  if (rows == 0 || cols == 0) return -1;

  // var: result column; initialize to -1
  let resCol = -1;
  // var: row idx; initialize to first col
  let row = 0;
  // var: col idx; initialize to last col
  let col = cols - 1
  // loop until exceeding row or col idx
  while (row < rows && col >= 0) {
    // if: element is 1; update resCol and move left
    if (binaryMatrix.get(row, col) == 1) {
      resCol = col;
      col--;
      // else: element is 0; move down
    } else {
      row++;
    }
  }

  // return resCol
  return resCol;
};