class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)

    if head is None: 
        return new_node

    if position == 0:
        new_node.next = head
        return new_node
    
    cur_node = head
    for _ in range(position-1):
        cur_node = cur_node.next
    
    next_node = cur_node.next
    cur_node.next = new_node
    new_node.next = next_node
    
    return head
    