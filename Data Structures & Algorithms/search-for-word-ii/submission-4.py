class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        words = set(words)
        max_len = max(len(w) for w in words)

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        res = set()

        def dfs(r, c, cur_word):
            if (
                r < 0 or c < 0 or
                r >= len(board) or c >= len(board[0]) or
                visited[r][c]
            ):
                return

            cur_word += board[r][c]

            if len(cur_word) > max_len:
                return

            if cur_word in words:
                res.add(cur_word)

            visited[r][c] = True

            for dr, dc in directions:
                dfs(r + dr, c + dc, cur_word)

            visited[r][c] = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "")

        return list(res)