function delayCounter(target, wait) {
  let num = 1;
  return function() {
    const timer = setInterval(() => {
      console.log(num);
      if (num === target) {
        clearInterval(timer);
        return;
      }
      num++;
    }, wait)
  }
}

const countLogger = delayCounter(3, 1000)
countLogger();
// After 1 second, log 1
// After 2 seconds, log 2
// After 3 seconds, log 3