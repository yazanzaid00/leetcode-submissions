class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isNum(char:str)-> bool:
            return "1" <= char <= "9"
        rows_set = [set() for _ in range(len(board))]
        cols_set = [set() for _ in range(len(board[0]))]
        boxes_set  = [[set() for _ in range(0, len(board[0]), 3)] for _ in range(0, len(board), 3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not isNum(board[i][j]):
                    continue
                
                box_row, box_col = i//3, j//3
                if board[i][j] in rows_set[i] or\
                   board[i][j] in cols_set[j] or\
                   board[i][j] in boxes_set[box_row][box_col]:
                   return False
                rows_set[i].add(board[i][j])
                cols_set[j].add(board[i][j])
                boxes_set[box_row][box_col].add(board[i][j])
        return True