class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row_hash = {}
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                else:
                    if val in row_hash:
                        return False
                    else:
                        row_hash[val] = 1

        for i in range(9):
            col_hash = {}
            for j in range(9):
                val = board[j][i]
                if val == ".":
                    continue
                else:
                    if val in col_hash:
                        return False
                    else:
                        col_hash[val] = 1

        for i in range(3):
            for j in range(3):
                seen = {}
                for r in range(i*3, i*3+3):
                    for c in range(j*3, j*3+3):
                        if board[r][c] == ".":
                            continue
                        if seen.get(board[r][c], 0):
                            return False
                        else:
                            seen[board[r][c]] =1

        return True
        

