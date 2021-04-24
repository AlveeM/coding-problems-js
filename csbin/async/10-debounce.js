function debounce(callback, interval) {
  let timer;
  let isIntervalElapsed = true;
  return function() {
    if (isIntervalElapsed) {
      isIntervalElapsed = false;
      return callback();
    }

    clearTimeout(timer);
    timer = setTimeout(() => {
      isIntervalElapsed = true;
    }, interval);
  }
}

function giveHi() { return 'hi'; }
const giveHiSometimes = debounce(giveHi, 3000);
console.log(giveHiSometimes()); // -> 'hi'
setTimeout(function() { console.log(giveHiSometimes()); }, 2000); // -> undefined
setTimeout(function() { console.log(giveHiSometimes()); }, 4000); // -> undefined
setTimeout(function() { console.log(giveHiSometimes()); }, 8000); // -> 'hi'