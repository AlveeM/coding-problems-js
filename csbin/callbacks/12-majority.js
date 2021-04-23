function majority(array, callback) {
	count = {
    true: 0,
    false: 0
  }
  
  array.forEach(el => count[callback(el)]++)
  
  if (count[true] > count[false]) {
    return true;
  } else {
    return false;
  }
}

const isOdd = function(num) { return num % 2 === 1; };
console.log(majority([1, 2, 3, 4, 5], isOdd)); // should log: true
console.log(majority([2, 3, 4, 5], isOdd)); // should log: false