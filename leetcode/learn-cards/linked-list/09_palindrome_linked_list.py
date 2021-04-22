class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        
        def isPalindromeRec(node):
            if node is not None: 
                if not isPalindromeRec(node.next):
                    return False
                if self.left.val != node.val:
                    return False
                self.left = self.left.next
            
            return True
        
        return isPalindromeRec(head)

class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        
        mid = self.findMid(head)
        second_half_start = self.reverseList(mid.next)
        
        res = True
        left = head
        right = second_half_start
        while res and right:
            if left.val != right.val:
                res = False
            left = left.next
            right = right.next
            
        mid.next = self.reverseList(second_half_start)
        return res
    
    def findMid(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev