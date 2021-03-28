class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and self.dfs(r, c, 0):
                    return True
                    
        return False
    
    def dfs(self, r, c, idx):
        if idx == len(self.word):
            return True
        
        if self.isNotValid(r, c, idx):
            return False
        
        current_char = self.board[r][c]
        self.board[r][c] = ''
        
        hasWord = (self.dfs(r + 1, c, idx + 1) or
                  self.dfs(r - 1, c, idx + 1) or
                  self.dfs(r, c + 1, idx + 1) or
                  self.dfs(r, c - 1, idx + 1))
        
        self.board[r][c] = current_char
        return hasWord
        
    def isNotValid(self, r, c, idx):
        return (r < 0 or 
                r >= len(self.board) or
                c < 0 or
                c >= len(self.board[0]) or
                self.board[r][c] != self.word[idx])