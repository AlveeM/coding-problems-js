class TrieNode:
    def __init__(self):
        self.child = {}
        self.value = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.char_map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.char_map.get(key, 0)
        cur_node = self.root
        self.char_map[key] = val
        cur_node.value += delta
        for char in key:
            if char not in cur_node.child:
                cur_node.child[char] = TrieNode()
            cur_node = cur_node.child[char]
            cur_node.value += delta

    def sum(self, prefix: str) -> int:
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.child:
                return 0
            cur_node = cur_node.child[char]
        return cur_node.value
