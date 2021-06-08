function rollCall(names) {
  i = 0;
  return function() {
    if (i >= names.length) {
      console.log('Everyone accounted for');
      return;
    }
    console.log(names[i]);
    i++;
  }
}

const rollCaller = rollCall(['Victoria', 'Juan', 'Ruth'])
rollCaller() // => should log 'Victoria'
rollCaller() // => should log 'Juan'
rollCaller() // => should log 'Ruth'
rollCaller() // => should log 'Everyone accounted for'