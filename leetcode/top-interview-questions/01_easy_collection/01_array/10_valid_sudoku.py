class Solution:
    def isValidSudoku(self, board):
        rows = set()
        cols = set()
        squares = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    r_key = (i, num)
                    c_key = (j, num)
                    s_key = (i//3, j//3, num)
                    
                    if (r_key in rows
                        or c_key in cols
                        or s_key in squares):
                        return False
                    
                    rows.add(r_key)
                    cols.add(c_key)
                    squares.add(s_key)
                    
        return True