const DoublyLinkedList = function() {
  const dList = {
    head: null,
    tail: null
  }

  dList.add = value => {
    const newNode = {
      value,
      next: null,
      previous: null
    }

    if (dList.tail == null) {
      dList.head = newNode;
    } else {
      newNode.previous = dList.tail;
      newNode.previous.next = newNode;
    }

    dList.tail = newNode;
    return newNode;
  }

  dList.removeHead = () => {
    if (dList.head == null) {
      return
    }

    if (dList.head === dList.tail) {
      dList.head = null;
      dList.tail = null;
      return;
    }

    const removeNode = dList.head;
    dList.head = removeNode.next;
    removeNode.next = null;
    dList.head.previous = null;
  }

  return dList;
}


/**
 * @param {number[]} nums
 */
var FirstUnique = function (nums) {
  this.hash = {}
  this.dList = new DoublyLinkedList();
  for (let i in nums) {
    this.add(nums[i]);
  }
};

/**
 * @return {number}
 */
FirstUnique.prototype.showFirstUnique = function () {
  let firstUnique = -1;
  let curNode = this.dList.head;
  while(curNode != null) {
    if(this.hash[curNode.value].value == null) {
      curNode = curNode.next;
      this.dList.removeHead();
    } else {
      return curNode.value;
    }
  }
  return firstUnique;
};

/**
 * @param {number} value
 * @return {void}
 */
FirstUnique.prototype.add = function (value) {
  if(this.hash[value]) {
    this.hash[value] = {value: null, next: null, previous: null}
  } else {
    this.hash[value] = this.dList.add(value)
  }
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * var obj = new FirstUnique(nums)
 * var param_1 = obj.showFirstUnique()
 * obj.add(value)
 */