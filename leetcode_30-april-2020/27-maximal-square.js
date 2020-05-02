/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function (matrix) {
  let r = matrix.length;
  if (r == 0) return 0;
  let c = matrix[0].length;
  if (c == 0) return 0;

  let maxSquare = 0;
  let solArr = Array(c).fill(0);
  let diag = matrix[0][0] == '0' ? 0 : 1;

  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      let prevDiag = solArr[j];
      if (i == 0 || j == 0) {
        if (matrix[i][j] == '1') {
          solArr[j] = 1;
          maxSquare = Math.max(maxSquare, solArr[j]);
        } else {
          solArr[j] = 0;
        }
      } else {
          if (matrix[i][j] == '1') {
            solArr[j] = 1 + Math.min(solArr[j], solArr[j-1], diag);
            maxSquare = Math.max(maxSquare, solArr[j]);
          } else {
            solArr[j] = 0;
          }
      }
      diag = (j == c-1) ? solArr[0] : prevDiag;
    }
  }

  return maxSquare * maxSquare;
};