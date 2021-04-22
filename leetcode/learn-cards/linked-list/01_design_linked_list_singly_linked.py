class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self.getNodeAtIndex(index)
        if cur is not None:
            return cur.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        return

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            self.addAtHead(val)
            return
    
        new_node = Node(val)
        old_tail = self.getTail()
        old_tail.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return 
        
        prev = self.getNodeAtIndex(index - 1)
        if prev is None:
            return
        
        new_node = Node(val)
        next_node = prev.next
        new_node.next = next_node
        prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        cur = self.getNodeAtIndex(index)
        if cur is None:
            return
        
        prev = self.getNodeAtIndex(index - 1)
        next_node = cur.next
        
        if prev is not None:
            prev.next = next_node
        else:
            self.head = next_node
    
    def getNodeAtIndex(self, index: int) -> 'Node':
        if index < 0: 
            return None
        
        cur = self.head
        i = 0
        while i < index and cur is not None:
            cur = cur.next
            i += 1
        return cur
    
    def getTail(self) -> 'Node':
        cur = self.head
        while cur is not None and cur.next is not None:
            cur = cur.next
        return cur