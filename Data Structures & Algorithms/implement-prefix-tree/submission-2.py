class PrefixNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = dict() if children is None else children
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.__root = PrefixNode()

    def insert(self, word: str) -> None:
        cur_node = self.__root
        for i in range(len(word)):
            if word[i] not in cur_node.children:
                new_node = PrefixNode(word[i])
                cur_node.children[word[i]] = new_node
            cur_node = cur_node.children[word[i]]
        cur_node.is_word = True
            

    def search(self, word: str) -> bool:
        cur_node = self.__root
        for i in range(len(word)):
            if word[i] not in cur_node.children:
                return False
            cur_node = cur_node.children[word[i]]
        return cur_node.is_word == True

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.__root
        for i in range(len(prefix)):
            if prefix[i] not in cur_node.children:
                return False
            cur_node = cur_node.children[prefix[i]]
        return True

        
        