function mapWith(array, callback) {
	const result = [];
  array.forEach(el => result.push(callback(el)));
  return result;
}

// console.log(mapWith([1, 2, 3], addTwo));