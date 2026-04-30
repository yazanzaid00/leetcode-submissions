from typing import List, Dict, Optional


class TrieNode:
    def __init__(self) -> None:
        # children: mapping char -> TrieNode
        self.children: Dict[str, "TrieNode"] = {}
        # store index of the word in the original `words` list
        # -1 means "no word ends here"
        self.word_index: int = -1

    def insert(self, word: str, index: int) -> None:
        """
        Insert `word` into the trie.
        Q: As you walk each character, when do you create a new child node?
        """
        node: TrieNode = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # At the end of the word, mark that a word ends here
        node.word_index = index


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Basic sanity: empty input edge cases
        if not board or not board[0] or not words:
            return []

        rows, cols = len(board), len(board[0])

        # 1) Build trie from all words
        root = TrieNode()
        for i, w in enumerate(words):
            # (Optional thought: would you skip inserting words longer than rows*cols?)
            root.insert(w, i)

        found_indices: List[int] = []          # we will store word indices here
        # Alternative: you could use a set to avoid duplicates if you don't clear word_index.

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int, node: TrieNode) -> None:
            """
            DFS from cell (r, c) assuming we are at trie node `node`.

            Key questions to guide your implementation:

            Q1 (pruning / base cases):
                - When should we *immediately* return?
                  Think about:
                    * r/c out of [0..rows-1]/[0..cols-1]
                    * cell already visited (how will you mark this?)
                    * board[r][c] not in node.children (no word has this prefix)
                TODO: implement these guard checks and 'return' when needed.

            Q2 (advance in trie):
                - Let ch = board[r][c].
                - How do you move to the child trie node corresponding to ch?
                TODO: set `next_node` appropriately.

            Q3 (word found):
                - How do you know if `next_node` represents the end of some word?
                - How do you avoid adding the same word multiple times?
                  (Hint: use `word_index` and then set it to -1 after using it.)
                TODO: if a word is found, append its index to `found_indices`.

            Q4 (visited marking / backtracking):
                - How do you prevent revisiting (r, c) in this path?
                  (Common trick: temporarily set board[r][c] = '#'.)
                - After exploring neighbors, you must restore the original character.
                TODO: implement the mark -> recurse -> unmark pattern.

            Q5 (neighbor exploration):
                - For each (dr, dc) in `directions`, recurse to (r + dr, c + dc).
                  With which trie node should you recurse?
            """
            # === TODO: remove 'pass' and implement the logic described above ===

            # Key questions to guide your implementation:

            # Q1 (pruning / base cases):
            #     - When should we *immediately* return?
            #       Think about:
            #         * r/c out of [0..rows-1]/[0..cols-1]
            #         * cell already visited (how will you mark this?)
            #         * board[r][c] not in node.children (no word has this prefix)
            #     TODO: implement these guard checks and 'return' when needed.
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == "#" or board[r][c] not in node.children:
                return False
            # Q2 (advance in trie):
            #     - Let ch = board[r][c].
            #     - How do you move to the child trie node corresponding to ch?
            #     TODO: set `next_node` appropriately.
            ch = board[r][c]
            node = node.children[ch]
            # Q3 (word found):
            #     - How do you know if `next_node` represents the end of some word?
            #     - How do you avoid adding the same word multiple times?
            #       (Hint: use `word_index` and then set it to -1 after using it.)
            #     TODO: if a word is found, append its index to `found_indices`.
            if node.word_index != -1:
                found_indices.append(node.word_index)
                node.word_index = -1
            # Q4 (visited marking / backtracking):
            #     - How do you prevent revisiting (r, c) in this path?
            #       (Common trick: temporarily set board[r][c] = '#'.)
            #     - After exploring neighbors, you must restore the original character.
            #     TODO: implement the mark -> recurse -> unmark pattern.
            temp = board[r][c]
            board[r][c] = '#'
            # Q5 (neighbor exploration):
            #     - For each (dr, dc) in `directions`, recurse to (r + dr, c + dc).
            #       With which trie node should you recurse?
            for dr, dc in directions:
                dfs(r + dr, c + dc, node)
            board[r][c] = temp
        # 2) Start DFS from every cell as a potential starting point
        for r in range(rows):
            for c in range(cols):
                # Thought: Do you want an early check here (e.g. board[r][c] in root.children)?
                # That can prune starting points that cannot start any word.
                dfs(r, c, root)

        # 3) Convert collected indices back to words
        # If you used an index only once per word (by clearing word_index),
        # you don't need to deduplicate here.
        result: List[str] = [words[i] for i in found_indices]
        return result
