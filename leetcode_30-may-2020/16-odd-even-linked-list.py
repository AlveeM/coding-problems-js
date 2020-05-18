from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head

        h_odd = head
        h_even = head.next
        odd = h_odd
        even = h_even

        while even is not None:
            if even.next is not None:
                odd.next = even.next
            else:
                odd.next = h_even
                return h_odd
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = h_even
        return h_odd