class Solution:
    def reverseBetween(self, head, m, n):
        if m == n: return head
        
        prev = None
        cur = head
        for _ in range(m-1):
            prev = cur
            cur = cur.next
            
        last_node_left_part = prev
        last_node_sub_list = cur
        
        next_node = None
        for _ in range(n-m+1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        if last_node_left_part:
            last_node_left_part.next = prev
        else:
            head = prev
        
        last_node_sub_list.next = cur
        
        return head