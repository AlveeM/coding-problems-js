class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        return prev

class Solution2:
    def reverseList(self, head):
        if not head or not head.next: return head
        
        reversed_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return reversed_node