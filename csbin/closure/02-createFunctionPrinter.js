function createFunctionPrinter(input) {
  return function() {
    console.log(input);
  }
}

const printSample = createFunctionPrinter('sample');
printSample(); // => should console.log('sample');
const printHello = createFunctionPrinter('hello');
printHello(); // => should console.log('hello');