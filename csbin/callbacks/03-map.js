function map(array, callback) {
	const result = [];
  for (const el of array) {
    result.push(callback(el));
  }
  return result;
}

// console.log(map([1, 2, 3], addTwo));