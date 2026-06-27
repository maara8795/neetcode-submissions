class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row_hash = {}
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if row_hash.get(val, 0):
                    return False
                row_hash[val] = 1

        for i in range(9):
            column_hash = {}
            for j in range(9):
                val = board[j][i]
                if val == ".":
                    continue
                if column_hash.get(val, 0):
                    return False
                column_hash[val] = 1

        for box_row in range(3):
            for box_col in range(3):
                seen = {}
                for r in range(box_row * 3, box_row * 3 + 3):
                    for c in range(box_col * 3, box_col * 3 + 3):
                        if board[r][c]== ".":
                            continue
                        if seen.get(board[r][c], 0):
                            return False
                        else:
                            seen[board[r][c]] = 1

        return True
