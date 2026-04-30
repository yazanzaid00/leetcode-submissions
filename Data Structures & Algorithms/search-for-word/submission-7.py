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
            if min(row, col) < 0 or \
                row >= len(board) or \
                col >= len(board[0]) or \
                board[row][col] == '#' or \
                board[row][col] != word[i]:
                return False
            if i == len(word) - 1 and word[i] == board[row][col]:
                return True
            temp = board[row][col]
            board[row][col] = '#'
            for d_row, d_col in directions:
                new_row, new_col = row + d_row, col + d_col
                if word_exist(new_row, new_col, i + 1):
                    board[row][col] = temp
                    return True
            board[row][col] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word_exist(i, j, 0):
                     return True
        return False