/**
 * @param {number[]} arr
 * @return {number}
 */
var countElements = function (arr) {
  // declare variable: zero; store element count
  let count = 0;
  // declare variable: empty object; store elements as keys
  let obj = {};

  // iterate over arr
  for (let el of arr) {
    // initialize each element as key of obj
    obj[el] ? obj[el]++ : obj[el] = 1;
  }

  // iterate over arr
  for (let el of arr) {
    // if el + 1 is an obj key
      // increment count
    if (el + 1 in obj) {
      count++;
    }
  }

  // return count of elements
  return count;
};

let arr = [1,3,2,3,5,0];
console.log(countElements(arr)); // 3

arr = [1,1,3,3,5,5,7,7];
console.log(countElements(arr)); // 0

arr = [];
console.log(countElements(arr)); // 0

arr = [1,1,2,2];
console.log(countElements(arr)); // 2