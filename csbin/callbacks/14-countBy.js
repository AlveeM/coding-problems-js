function countBy(array, callback) {
  return array.reduce((res, el) => {
    const key = callback(el);
    res[key] = res[key] !== undefined ? ++res[key] : 1;
    return res;
  }, {})
}

// /*** Uncomment these to check your work! ***/
console.log(countBy([1, 2, 3, 4, 5], function(num) {
if (num % 2 === 0) return 'even';
else return 'odd';
})); // should log: { odd: 3, even: 2 }