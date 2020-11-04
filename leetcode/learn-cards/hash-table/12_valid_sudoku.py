class Solution:
    def isValidSudoku(self, board):
        row, col, square = set(), set(), set()

        for i in range(9):
            for j in range(9):
                cur_el = board[i][j]
                if cur_el != '.':
                    r_key = (i, cur_el)
                    c_key = (j, cur_el)
                    s_key = (i//3, j//3, cur_el)
                    
                    if (r_key in row 
                            or c_key in col
                            or s_key in square):
                        return False
                    
                    row.add(r_key)
                    col.add(c_key)
                    square.add(s_key)
        
        return True
        