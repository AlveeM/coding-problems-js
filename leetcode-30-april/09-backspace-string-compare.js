/**
 * @param {string} S
 * @param {string} T
 * @return {boolean}
 */
var backspaceCompare = function (S, T) {
  // declare var: char index of S; initialize to last index
  let idxS = S.length - 1;
  // declare var: char index of T; initialize to last index
  let idxT = T.length - 1;
  // loop over S and T until either index reaches 0
  while (idxS >= 0 || idxT >= 0) {
    // declare var: new char index of S skipping backspace
    let newIdxS = getNextCharIdx(S, idxS);
    // declare var: new char index of T skipping backspace
    let newIdxT = getNextCharIdx(T, idxT);
    // if: end of both strings; true
    if (newIdxS < 0 && newIdxT < 0) return true;
    // if: end of one string; false
    if (newIdxS < 0 || newIdxT < 0) return false;
    // if: chars not equal at new position; false
    if (S[newIdxS] != T[newIdxT]) return false;
    // assign var: index of S to new index - 1
    idxS = newIdxS - 1;
    // assign var: index of T to new index - 1
    idxT = newIdxT - 1;
  }
  // return true
  return true;
};

var getNextCharIdx = function (str, idx) {
  // declare var: track backspace count; initialize to 0
  let bsCount = 0;
  // loop while true
  while (true) {
    // if: backspace character; ++ backspace count
    if (str[idx] == '#') {
      bsCount++;
      // elif: backspace count > 0; -- backspace count
    } else if (bsCount > 0) {
      bsCount--;
      // else: exit loop
    } else break;
    // decrement idx
    idx--;
  }
  // return idx
  return idx;
}

var S = "ab#c";
var T = "ad#c";
console.log(backspaceCompare(S, T)); // true

S = "ab##";
T = "c#d#";
console.log(backspaceCompare(S, T)); // true

S = "a##c";
T = "#a#c";
console.log(backspaceCompare(S, T)); // true

S = "a#c";
T = "b";
console.log(backspaceCompare(S, T));; // false