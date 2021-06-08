function once(func) {
  let called = false;
  let res;
  return function(val) {
    if (!called) {
      res = func(val);
      called = true;
    }
    return res;
  }
}

const addByTwo = num => num + 2;
const onceFunc = once(addByTwo);
console.log(onceFunc(4));  // => should log 6
console.log(onceFunc(10));  // => should log 6
console.log(onceFunc(9001));  // => should log 6