function createFunction() {
  return function() {
    console.log("hello")
  }
}

const function1 = createFunction();
function1(); // => should console.log('hello');