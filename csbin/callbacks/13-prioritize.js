function prioritize(array, callback) {
	const res = {
    true: [],
    false: []
  }
  
	array.forEach(el => res[callback(el)].push(el));
	return res[true].concat(res[false]);
}

// /*** Uncomment these to check your work! ***/
const startsWithS = function(str) { return str[0] === 's' || str[0] === 'S'; };
console.log(prioritize(['curb', 'rickandmorty', 'seinfeld', 'sunny', 'friends'], startsWithS)); 
// should log: ['seinfeld', 'sunny', 'curb', 'rickandmorty', 'friends']
