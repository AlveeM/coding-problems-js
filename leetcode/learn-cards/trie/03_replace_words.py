class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word = True
        cur.word = word
        
    def findWord(self, word):
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
                if cur.is_word:
                    return cur.word
            else:
                return ""
        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for word in dictionary:
            trie.insertWord(word)
            
        sentence = sentence.split(" ")
        
        for i in range(len(sentence)):
            root_word = trie.findWord(sentence[i])
            if root_word != "":
                sentence[i] = root_word
        return " ".join(sentence)