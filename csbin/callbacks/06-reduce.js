function reduce(array, callback, initialValue) {
	for (let i = 0; i < array.length; i++) {
      initialValue = callback(initialValue, array[i]);
  }
  return initialValue;
}

const add = (acc, el) => acc + el;
console.log(reduce([1, 2, 3], add, 0));