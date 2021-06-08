function callTimes() {
  let numCalled = 0;
  return function() {
    numCalled++;
    return numCalled;
  }
}

let myNewFunc1 = callTimes();
let myNewFunc2 = callTimes();
console.log(myNewFunc1()); // => 1
console.log(myNewFunc1()); // => 2
console.log(myNewFunc2()); // => 1
console.log(myNewFunc2()); // => 2