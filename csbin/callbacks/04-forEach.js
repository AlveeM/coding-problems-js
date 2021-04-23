function forEach(array, callback) {
	for (let i = 0; i < array.length; i++) {
    callback(array[i], i, array);
  }
}

// forEach([1, 2, 3], (el) => console.log(el))