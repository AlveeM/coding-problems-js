class Solution:
    def distributeCoins(self, root):
        self.moves = 0
        self.countMoves(root)
        return self.moves
    
    def countMoves(self, node):
        if node is None: return 0
        
        leftCount = self.countMoves(node.left)
        rightCount = self.countMoves(node.right)
        self.moves += abs(leftCount) + abs(rightCount)
        
        return node.val + leftCount + rightCount - 1