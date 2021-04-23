function highestFunc(objOfFuncs, subject) {
  const keys = Object.keys(objOfFuncs);
	return keys.reduce((prevKey, key) => {
    const prevFuncRes = objOfFuncs[prevKey](subject);
    const curFuncRes = objOfFuncs[key](subject);
    if (curFuncRes > prevFuncRes) {
      return key;
    } else {
      return prevKey;
    }
  }, keys[0])
}

const groupOfFuncs = {};
groupOfFuncs.double = n => n * 2;
groupOfFuncs.addTen = n => n + 10;
groupOfFuncs.inverse = n => n * -1;
console.log(highestFunc(groupOfFuncs, 5)); // should log: 'addTen'
console.log(highestFunc(groupOfFuncs, 11)); // should log: 'double'
console.log(highestFunc(groupOfFuncs, -20)); // should log: 'inverse'