class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head is None or head.next is None): return head
        
        reversedHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return reversedHead

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prevNode = None

#         while head.next:
#             next_node = head.next
#             head.next = prevNode
#             prevNode = head
#             head = next_node

#         return head