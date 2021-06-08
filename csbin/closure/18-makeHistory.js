function makeHistory(limit) {
	let history = [];
  return function (input) {
    if (input === 'undo') {
      if (history.length === 0) return 'nothing to undo';
      const lastWord = history.pop();
      return `${lastWord} undone`;s
    } 
    history.push(input);
    if (history.length > limit) {
      history = history.slice(1);
    }
		return `${input} done`;
  }
}

// /*** Uncomment these to check your work! ***/
const myActions = makeHistory(2);
console.log(myActions('jump')); // => should log 'jump done'
console.log(myActions('undo')); // => should log 'jump undone'
console.log(myActions('walk')); // => should log 'walk done'
console.log(myActions('code')); // => should log 'code done'
console.log(myActions('pose')); // => should log 'pose done'
console.log(myActions('undo')); // => should log 'pose undone'
console.log(myActions('undo')); // => should log 'code undone'
console.log(myActions('undo')); // => should log 'nothing to undo'