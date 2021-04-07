class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word = True

    def search(self, word: str) -> bool:
        def searchRec(i, trie):
            if i == len(word):
                return trie.is_word
            
            # search all children if current char is "."
            if word[i] == ".":      
                for val in trie.children.values():
                    if searchRec(i + 1, val):
                        return True
                return False
            
            if word[i] not in trie.children:
                    return False
            
            return searchRec(i + 1, trie.children[word[i]])
        
        return searchRec(0, self.root)