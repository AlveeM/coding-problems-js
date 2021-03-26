from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        
        q = deque()
        q.append(root)
        
        while q:
            n = len(q)
            level = []
            
            for _ in range(n):
                node = q.popleft()
                level.append(node)
                
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
        
        return root

class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root 