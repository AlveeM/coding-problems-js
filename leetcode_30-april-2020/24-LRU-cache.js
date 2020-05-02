/**
 * @param {number} capacity
 */
var LRUCache = function (capacity) {
  this.capacity = capacity;
  this.length = 0;
  this.hash = {};
  this.head = new Node();
  this.tail = new Node();
  this.head.next = this.tail;
  this.tail.prev = this.head;
};
/**
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function (key) {
  if (!(key in this.hash)) {
    return -1;
  }
  removeNode(this.hash[key]);
  insertAfter(this.hash[key], this.head);
  return this.hash[key].val;
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function (key, value) {
  if (!(key in this.hash)) {
    this.hash[key] = new Node(key, value);
    this.length += 1;
  } else {
    this.hash[key].val = value;
    removeNode(this.hash[key]);
  }

  insertAfter(this.hash[key], this.head);

  if (this.length > this.capacity) {
    delete this.hash[this.tail.prev.key];
    this.length -= 1;
    removeNode(this.tail.prev);
  }
};

function insertAfter(a, b) {
  a.next = b.next;
  a.next.prev = a;
  b.next = a;
  a.prev = b;
}

function removeNode(node) {
  node.prev.next = node.next;
  node.next.prev = node.prev;
}

class Node {
  constructor(key, val) {
    this.key = key;
    this.val = val;
    this.prev = null;
    this.next = null;
  }
}