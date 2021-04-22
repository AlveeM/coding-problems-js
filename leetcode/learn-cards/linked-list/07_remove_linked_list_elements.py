class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            
            cur = cur.next
            
        return dummy.next

class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        
        head.next = self.removeElements(head.next, val)
        
        if head.val == val:
            return head.next
        
        return head