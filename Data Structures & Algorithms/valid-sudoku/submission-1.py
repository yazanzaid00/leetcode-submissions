class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isNum(num: str) -> bool:
            return "1" <= num <= "9"
        # check for duplicates in row
        for row in board:
            row_set = set()
            for j in range(len(board[0])):
                if isNum(row[j]):
                    if row[j] in row_set:
                        return False
                    row_set.add(row[j])

        # check for duplicates in col
        for j in range(len(board[0])):
            col_set = set()
            for i in range(len(board)):
                if isNum(board[i][j]):
                    if board[i][j] in col_set:
                        return False
                    col_set.add(board[i][j])

        # check for duplicates in 3x3 boards
        # iterate over all 3x3 board
        for start_row in range(0, len(board), 3):
            for start_col in range(0, len(board[0]), 3):
                # check 3x3 board
                board_set = set()
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if isNum(board[i][j]):
                            if board[i][j] in board_set:
                                return False
                            board_set.add(board[i][j])

        return True