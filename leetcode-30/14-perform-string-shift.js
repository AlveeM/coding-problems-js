/**
 * @param {string} s
 * @param {number[][]} shift
 * @return {string}
 */
var stringShift = function(s, shift) {
  // var: store string length
  const len = s.length;
  // var: track final shift
  let fS = 0;
  // iterate over shift
  for (let arr of shift) {
    // if: arr[0] == 0; decrement final shift
    if (arr[0] == 0) {
      fS -= arr[1];
      // else: increment final shift
    } else {
      fS += arr[1];
    }

  }

  // normalize final shift if abs(fs) > len
  fS = fS % len;

  // if: right shift
  if (fS > 0) {
    // var: index at which string will be split
    const idx = len - fS;
    // var: perform rotation
    const result = s.substring(idx) + s.substring(0, idx);
    // return result
    return result;
    // else if: left shift
  } else if (fS < 0) {
    // make final shift value absolute
    fS = Math.abs(fS);
    // perform rotation
    const result = s.substring(fS) + s.substring(0, fS);
    // return result
    return result;
  }
  // return string
  return s;
};

let s = 'abc';
let shift = [[0, 1], [1, 2]];
console.log(stringShift(s, shift)); // 'cab'

s = 'abcdefg';
shift = [[1,1],[1,1],[0,2],[1,3]];
console.log(stringShift(s, shift)); // 'efgabcd'

s = 'wpdhhcj';
shift = [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]];
console.log(stringShift(s, shift)); // 'hcjwpdh'