class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

def reverse(head):
    prev_node = None
    cur_node = head
    while cur_node:
        # update next and prev links
        prev_node = cur_node.prev
        cur_node.prev = cur_node.next
        cur_node.next = prev_node
        # move cur_node to next element
        cur_node = cur_node.prev
    
    if prev_node:
        head = prev_node.prev

    return head