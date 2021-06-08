function russianRoulette(num) {
  let timesCalled = 0;
  return function() {
    timesCalled++;
    if (timesCalled === num) {
      return 'bang';
    } else if(timesCalled > num) {
      return 'reload to play again';
    } else {
      return 'click';
    }
  }
}

const play = russianRoulette(3);
console.log(play()); // => should log 'click'
console.log(play()); // => should log 'click'
console.log(play()); // => should log 'bang'
console.log(play()); // => should log 'reload to play again'
console.log(play()); // => should log 'reload to play again'