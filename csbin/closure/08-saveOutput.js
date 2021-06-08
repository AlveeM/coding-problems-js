function saveOutput(func, magicWord) {
  const tracker = {};
  return function(val) {
    if (val === magicWord) return tracker;
    tracker[val] = func(val);
    return tracker[val];
  }
}

const multiplyBy2 = function(num) { return num * 2; };
const multBy2AndLog = saveOutput(multiplyBy2, 'boo');
console.log(multBy2AndLog(2)); // => should log 4
console.log(multBy2AndLog(9)); // => should log 18
console.log(multBy2AndLog('boo')); // => should log { 2: 4, 9: 18 }