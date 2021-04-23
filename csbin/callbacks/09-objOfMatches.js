function objOfMatches(array1, array2, callback) {
  return array1.reduce((res, el, i) => {
    if (callback(el) === array2[i]) {
      res[el] = array2[i];
    }
    return res;
  }, {})
}

console.log(objOfMatches(['hi', 'howdy', 'bye', 'later', 'hello'], ['HI', 'Howdy', 'BYE', 'LATER', 'hello'], function(str) { return str.toUpperCase(); })); // should log: { hi: 'HI', bye: 'BYE', later: 'LATER' }