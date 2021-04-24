function forEach(array, callback, thisArg) {
	for (let i = 0; i < array.length; i++) {
    if (thisArg !== undefined) {
      callback.call(thisArg, array[i], i, array);
    } else {
      callback(array[i], i, array);
    }
  }
}

forEach([1, 2, 3], (el) => console.log(el))