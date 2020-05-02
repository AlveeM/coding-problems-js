/**
 * @param {string} s
 * @return {boolean}
 */
// track parens in a count parameter
// iterate over string and update count based on current char
// for * check all possibilities
var checkValidString = function (s, count=0) {
  for (let i = 0; i < s.length; i++) {
    // base case
    if (count < 0) {
      return false;
    }

    // var: store char at current idx
    const char = s[i];

    // if: '(' increment count and continue loop
    if (char == '(') {
      count++;
      continue;
    }

    // if: ')' decrement count and continue loop
    if (char == ')') {
      count--;
      continue;
    }

    // if: '*' check all possibilities:
      // +1 for '(', -1 for ')', count for ''
    const slicedS = s.slice(i + 1);
    return checkValidString(slicedS, count)
          || checkValidString(slicedS, count + 1)
          || checkValidString(slicedS, count - 1);
  }

  return count == 0;
};

console.log(checkValidString('()')); // true
console.log(checkValidString('(*)')); // true
console.log(checkValidString('(*))')); // true
console.log(checkValidString('((')); // false
console.log(checkValidString(')(')); // false