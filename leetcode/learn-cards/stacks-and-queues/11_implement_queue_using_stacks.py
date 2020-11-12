class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enq_stack = []
        self.deq_stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.enq_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.deq_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.deq_stack:
            while self.enq_stack:
                self.deq_stack.append(self.enq_stack.pop())

        return self.deq_stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.enq_stack and self.deq_stack