/**
 * @param {number[]} stones
 * @return {number}
 */

class maxHeap {
  constructor() {
    this.heap = [];
  }

  insert(val) {
    this.heap.push(val);
    this.__percolateUp(this.heap.length - 1);
  }

  getMax() {
    if (this.heap.length !== 0) {
      return this.heap[0]
    }
    return null;
  }

  removeMax() {
    if (this.heap.length > 1) {
      let max = this.heap[0];
      this.heap[0] = this.heap[this.heap.length - 1];
      this.heap.splice(this.heap.length - 1, 1);
      this.__maxHeapify(0)
      return max;
    } else if (this.heap.length === 1) {
      let max = this.heap[0];
      this.heap.splice(this.heap.length - 1, 1);
      return max;
    } else {
      return null;
    }
  }

  __percolateUp(index) {
    let parent = Math.floor((index - 1) / 2);
    if (index <= 0) {
      return;
    } else if (this.heap[parent] < this.heap[index]) {
      let tmp = this.heap[parent];
      this.heap[parent] = this.heap[index];
      this.heap[index] = tmp;
      this.__percolateUp(parent);
    }
  }

  __maxHeapify(index) {
    let left = (index * 2) + 1;
    let right = (index * 2) + 2;
    let largest = index;
    if ((this.heap.length > left) && (this.heap[largest] < this.heap[left])) {
      largest = left;
    }
    if ((this.heap.length > right) && (this.heap[largest] < this.heap[right])) {
      largest = right;
    }
    if (largest !== index) {
      let tmp = this.heap[largest];
      this.heap[largest] = this.heap[index];
      this.heap[index] = tmp;
      this.__maxHeapify(largest);
    }
  }

  buildHeap(arr) {
    this.heap = arr;
    for (let i = this.heap.length - 1; i >= 0; i--) {
      this.__maxHeapify(i);
    }
  }
}

var lastStoneWeight = function (stones) {
  // if: 1 stone; return stone
  if (stones.length == 1) return stones[0];
  // declare variables: biggest stone, second biggest stone, difference
  let max, secondMax, diff;
  // declare variable: a max heap
  const mh = new maxHeap();
  // populate max heap with stones
  mh.buildHeap(stones);
  // loop until there is one stone left in heap
  while (mh.heap.length > 1) {
    // assign var: max element of heap
    max = mh.removeMax();
    // assign var: second max element of heap
    secondMax = mh.removeMax();
    // if: both max element and second elment exist
    if (max && secondMax) {
      // assign var: diff updated; differene between max and second max
      diff = max - secondMax;
      // insert new stone in heap
      mh.insert(diff);
      // else: return max
    } else return max;
  }
  // if: heap has one element return element else return 0
  return mh.heap[0] ? mh.heap[0] : 0;
};

console.log(lastStoneWeight([2,7,4,1,8,1]));
console.log(lastStoneWeight([1,3]));