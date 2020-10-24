class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print(slow.data)
            return True

    return False

head = SinglyLinkedListNode(1)
head.next = SinglyLinkedListNode(2)
head.next.next = SinglyLinkedListNode(3)
head.next.next.next = SinglyLinkedListNode(4)
head.next.next.next.next = SinglyLinkedListNode(5)
# create cycle
head.next.next.next.next.next = head.next.next

print(has_cycle(head))