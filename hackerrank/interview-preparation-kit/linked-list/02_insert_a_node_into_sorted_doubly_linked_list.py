class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)

    # case 1: list is empty
    if head is None:
        head = new_node

    # case 2: new node inserted before head
    elif data <= head.data:
        new_node.next = head 
        head.prev = new_node
        head = new_node

    # case 3: insert in the correct position or at end
    else:
        cur_node = head
        while cur_node.next != None and cur_node.data < data:
            cur_node = cur_node.next
        
        # case 3a: insert at end
        if cur_node.next == None and cur_node.data < data:
            cur_node.next = new_node
            new_node.prev = cur_node

        # case 3b: insert between prev_node and cur_node
        else:
            prev_node = cur_node.prev

            # update previous node links
            prev_node.next = new_node
            new_node.prev = prev_node

            # update current node links
            new_node.next = cur_node
            cur_node.prev = new_node

    return head