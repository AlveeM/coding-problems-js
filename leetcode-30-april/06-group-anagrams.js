/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  // declare variable: obj for storing sorted string as key and an array of words as value
  const obj = {};
  // iterate over strs
  for (word of strs) {
    // declare varible: current word sorted in array
    let key = [...word].sort();
    // check if key exists in obj
      // exists: push current word to value arr
      // else: initialize to arr with current word
    obj[key] = obj[key] ? [...obj[key], word] : [word];
  }
  // return all the values of the obj
  return Object.values(obj);
};