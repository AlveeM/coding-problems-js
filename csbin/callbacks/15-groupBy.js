function groupBy(array, callback) {
  return array.reduce((res, el) => {
    const key = callback(el);
    if (res[key] !== undefined) {
      res[key].push(el);
    } else {
      res[key] = [el];
    };
    return res;
  }, {})
}

const decimals = [1.3, 2.1, 2.4];
const floored = function(num) { return Math.floor(num); };
console.log(groupBy(decimals, floored)); // should log: { 1: [1.3], 2: [2.1, 2.4] }