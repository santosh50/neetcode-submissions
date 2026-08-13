class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.endOfWord = True


    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return ptr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True

        
        