function objFilter(obj, callback) {
  return Object.keys(obj).reduce((res, key) => {
    if (callback(key) === obj[key]) {
      res[key] = obj[key];
    }
    return res;
  }, {});
}

const startingObj = {};
startingObj[6] = 3;
startingObj[2] = 1;
startingObj[12] = 4;
const half = n => n / 2;
console.log(objFilter(startingObj, half)); // should log: { 2: 1, 6: 3 }