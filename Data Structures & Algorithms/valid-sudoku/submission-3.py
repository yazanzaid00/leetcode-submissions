class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_sets = [set() for _ in range(len(board))]
        cols_sets = [set() for _ in range(len(board[0]))]
        sub_sets = [
            [set() for _  in range(len(board[0])//3)] for _ in range(len(board)//3)
        ]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows_sets[i]:
                    return False
                rows_sets[i].add(board[i][j])
        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in cols_sets[j]:
                    return False
                cols_sets[j].add(board[i][j])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                sub_i, sub_j = i//3, j//3
                if board[i][j] in sub_sets[sub_i][sub_j]:
                    return False
                sub_sets[sub_i][sub_j].add(board[i][j])
        return True