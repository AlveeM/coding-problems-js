function average() {
  const cache = {
    avg: 0,
    sum: 0,
    count: 0
  }
  return function(num) {
    if (num === undefined) {
      return cache.avg;
    } else {
      cache.sum += num;
      cache.count++;
      cache.avg = cache.sum / cache.count;
      return cache.avg;
    }
  }
}

const avgSoFar = average();
console.log(avgSoFar()); // => should log 0
console.log(avgSoFar(4)); // => should log 4
console.log(avgSoFar(8)); // => should log 6
console.log(avgSoFar()); // => should log 6
console.log(avgSoFar(12)); // => should log 8
console.log(avgSoFar()); // => should log 8