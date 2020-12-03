class Solution:
    def reverseKGroup(self, head, k):
        if not head or not head.next or k == 1: return head
        
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
            
        prev = None
        next = None
        newHead = None
        t1 = None
        t2 = head
        cur = head
        
        while (n >= k):
            for _ in range(k):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            
            if not newHead: newHead = prev
            if t1: t1.next = prev
            t2.next = cur
            t1 = t2
            t2 = cur
            prev = None
            n -= k
            
        return newHead