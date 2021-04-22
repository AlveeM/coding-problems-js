class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        odd_head = head
        even_head = head.next
        odd = odd_head
        even = even_head
        
        while even:
            if even.next:
                odd.next = even.next
            else:
                odd.next = even_head
                return odd_head
            
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return odd_head