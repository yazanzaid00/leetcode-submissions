class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def helper(curr, start_index):
            for i in range(start_index, len(word)):
                if word[i] == '.':
                    # we have multiple words to check, try each one...
                    for replace in curr.children.values():
                        if helper(replace, i + 1):
                            return True # propogate that we found one
                    # no replacements returned true so return False
                    return False

                elif word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]
            return curr.is_word
        return helper(self.root, 0)