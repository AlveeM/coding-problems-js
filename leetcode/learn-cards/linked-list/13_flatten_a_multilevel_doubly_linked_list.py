class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        self.flattenRec(head)
        return head
    
    def flattenRec(self, node):
        cur = node
        tail = node
        
        while cur:
            child = cur.child
            next_node = cur.next
            if child:
                new_tail = self.flattenRec(child)
                new_tail.next = next_node
                if next_node:
                    next_node.prev = new_tail
                cur.next = child
                child.prev = cur
                cur.child = None
                cur = tail
            else:
                cur = next_node
            
            if cur:
                tail = cur
        
        return tail

class Solution2:
    def flatten(self, head: 'Node') -> 'Node':
        
        def dfs(prev, curr):
            if not curr:
                return prev
            prev.next = curr
            curr.prev = prev
            rest = curr.next
            tail = dfs(curr, curr.child)
            curr.child = None
            return dfs(tail, rest)
        
        if not head:
            return head
        sentinel = Node()
        dfs(sentinel, head)
        sentinel.next.prev = None
        return sentinel.next