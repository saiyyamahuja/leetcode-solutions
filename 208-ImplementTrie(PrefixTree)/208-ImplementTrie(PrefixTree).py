class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True        

    def search(self, word: str) -> bool:
        node = self._findNode(word)
        return node is not None and node.is_end        

    def startsWith(self, prefix: str) -> bool:
        return self._findNode(prefix) is not None
    
    def _findNode(self, prefix: str):
        """Helper function to traverse the Trie."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node