class Node {
  constructor(value, next=null){
    this.value = value;
    this.next = next;
  }
}

/**
 * @param {Node} head
 * @return {Node}
 */
var middleNode = function (head) {
  // declare variable: slow pointer; initialized to head
  let slow = head;
  // declare variable: fast pointer; initialized to head
  let fast = head;
  // go through list until fast is null or reaches end of list
  while ((fast != null && fast.next != null)) {
    // move slow by one step
    slow = slow.next;
    // move fast by two steps
    fast = fast.next.next;
  }
  // return slow pointer
  return slow;
};

head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
console.log(`Middle Node: ${middleNode(head).value}`);
head.next.next.next.next.next = new Node(6);
console.log(`Middle Node: ${middleNode(head).value}`);
head.next.next.next.next.next.next = new Node(7);
console.log(`Middle Node: ${middleNode(head).value}`);