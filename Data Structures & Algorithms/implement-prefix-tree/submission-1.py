class TrieNode:
    def __init__(self, char=None):
        self._char = char
        self._children = dict()
        self._is_word = False

class PrefixTree:

    def __init__(self):
        self._root = TrieNode() # dictionary where character:children, the value are children of type prefix tree

    def insert(self, word: str) -> None:
        cur_node = self._root
        for i in range(len(word)):
            if word[i] not in cur_node._children:
                # add it to children
                next_node = TrieNode(word[i])
                cur_node._children[word[i]] = next_node
            cur_node = cur_node._children[word[i]]
        cur_node._is_word = True

    def search(self, word: str) -> bool:
        cur_node = self._root
        for i in range(len(word)):
            if word[i] not in cur_node._children:
                return False
            cur_node = cur_node._children[word[i]]
        return cur_node._is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self._root
        for i in range(len(prefix)):
            if prefix[i] not in cur_node._children:
                return False
            cur_node = cur_node._children[prefix[i]]
        return True