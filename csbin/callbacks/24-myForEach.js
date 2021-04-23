function myForEach(array, callback) {
	for (let i = 0; i < array.length; i++) {
    callback(array[i], i, array);
  }
}

let sum = 0;

function addToSum(num) {
  sum += num;
}

// /*** Uncomment these to check your work! ***/
const nums = [1, 2, 3];
myForEach(nums, addToSum);
console.log(sum); // Should output 6