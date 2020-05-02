/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var rangeBitwiseAnd = function (m, n) {
  // var: shift count
  let shifts = 0;

  // loop until m and n have the same number of bits
  while (m != n) {
    // right shift m by 1 bit
    m >>= 1;
    // right shift n by 1 bit
    n >>= 1;
    // increment shift count
    shifts++;
  }

  // return n with zero padding
  return n << shifts;
};

console.log(rangeBitwiseAnd(5, 7)); // 4