class TrieNode:
    def __init__(self, char=0):
        self.char = char
        self.children = {}
        self.is_word = False
class PrefixTree:

    def __init__(self):
        self.head = TrieNode() # add the first characters to it sentiel node

    def insert(self, word: str) -> None:
        cur = self.head
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]]= TrieNode(word[i])
            cur = cur.children[word[i]]
            if i == len(word) - 1:
                cur.is_word = True


    def search(self, word: str) -> bool:
        cur = self.head
        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]] 
            if i == len(word) - 1 and not cur.is_word:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]] 
        return True