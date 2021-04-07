class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words: return []
        
        trie = Trie(words)
            
        self.result = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(r, c, trie.root, "", board)
                
        return list(self.result)
    
    def dfs(self, r, c, trie, s, board):
        if trie.is_word:
            self.result.add(s)
            trie.is_word = False
        
        if self.isValidPos(r, c, board):
            char = board[r][c]
            child_node = trie.children.get(char)
            if child_node is not None:
                s += char
                board[r][c] = None
                
                self.dfs(r + 1, c, child_node, s, board)
                self.dfs(r - 1, c, child_node, s, board)
                self.dfs(r, c + 1, child_node, s, board)
                self.dfs(r, c - 1, child_node, s, board)
                
                board[r][c] = char
        
    def isValidPos(self, r, c, board):
        if not 0 <= r < len(board):
            return False
        if not 0 <= c < len(board[0]):
            return False
        if board[r][c] is None:
            return False
        return True
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self, words):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.is_word = True