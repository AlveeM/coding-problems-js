class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head is None or head.next is None): return head
        
        reversedList = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return reversedList

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None

        while head:
            cur_node = head
            head = head.next
            cur_node.next = prev_node
            prev_node = cur_node
        
        return prev_node
