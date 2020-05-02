/**
 * initialize your data structure here.
 */
var MinStack = function () {
  // constructor: min stack; initialized to []
  this.min = [];
  // constructor: main stack; initialized to []
  this.main = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function (x) {
  // push x into main stack
  this.main.push(x);
  // if: min stack is empty or x <= min stack element
  if (this.min.length == 0
    || x <= this.min[this.min.length - 1]
    ) {
      // push x into min stack
      this.min.push(x);
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
  // declare variable: store top elmeent of main stack
  var el = this.main.pop();
  // if: el is equal to min stack element
  if (el == this.min[this.min.length - 1]) {
    // pop from min stack
    this.min.pop();
  }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
  return this.main[this.main.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
  return this.min[this.min.length - 1];
};


var minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
console.log(minStack.getMin()); // --> Returns -3.
minStack.pop();
console.log(minStack.top());    // --> Returns 0.
console.log(minStack.getMin()); // --> Returns -2.