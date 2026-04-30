class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        directions =[
            (1, 0), #bottom
            (-1, 0), # up
            (0, 1), # right
            (0, -1) #left
        ]
        def word_exist(row: int, col: int, i: int):
            if i == len(word):
                return True
            # visited
            # how to mark as visited without affecting other checks? what is the idiomatic way?
            temp = board[row][col]
            board[row][col] = '#' #
            for d_row, d_col in directions:
                new_row, new_col = row + d_row, col + d_col
                if min(new_row, new_col) < 0 \
                        or new_row >= len(board) \
                        or new_col >= len(board[0]) \
                        or board[new_row][new_col] != word[i]:
                    continue
                if word_exist(new_row, new_col, i + 1):
                    board[row][col] = temp
                    return True # propogate True
            board[row][col] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and word_exist(i, j, 1):
                     return True
        return False