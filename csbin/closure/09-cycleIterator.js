function cycleIterator(array) {
  let i = 0;
  return function() {
    const curEl = array[i];
    if (i === array.length - 1) {
      i = 0;
      return curEl;
    }
    i++;
    return curEl;
  }
}

const threeDayWeekend = ['Fri', 'Sat', 'Sun'];
const getDay = cycleIterator(threeDayWeekend);
console.log(getDay()); // => should log 'Fri'
console.log(getDay()); // => should log 'Sat'
console.log(getDay()); // => should log 'Sun'
console.log(getDay()); // => should log 'Fri'