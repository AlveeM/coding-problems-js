import unittest

# Method 1: 
# - iterate over matrix each and if there's a zero mark its row and column 
# - iterate over the matrix and change an element to zero if its row or column is marked
# TC: O(n)
# SC: O(Height + Width)
def zero_matrix1(matrix):
    HEIGHT = len(matrix)
    WIDTH = len(matrix[0])
    zero_rows = [False] * HEIGHT
    zero_cols = [False] * WIDTH
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if matrix[row][col] == 0:
                zero_rows[row] = True
                zero_cols[col] = True
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if zero_rows[row] or zero_cols[col]:
                matrix[row][col] = 0

    return matrix

# Method 2:
# - when iterating over a row, check to see if it contains a zero and store a boolean in a variable
# - then iterate over the row again and set an element to zero if the row contains zero or the column contains zero
# TC: O(n)
# SC: O(Width)
def zero_matrix2(matrix):
    HEIGHT = len(matrix)
    WIDTH = len(matrix[0])
    zero_cols = [False] * WIDTH
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if matrix[row][col] == 0:
                zero_cols[col] = True
    for row in range(HEIGHT):
        row_contains_zero = False
        for col in range(WIDTH):
            if matrix[row][col] == 0:
                row_contains_zero = True
                break
        for col in range(WIDTH):
            if row_contains_zero or zero_cols[col]:
                matrix[row][col] = 0

    return matrix

# Method 3:
# - use the first row to keep track of columns that should contain zero
# - use the same method as Method 2 for tracking rows
# - update the first row at the end
# TC: O(n)
# SC: O(1)
def zero_matrix3(matrix):
    HEIGHT = len(matrix)
    WIDTH = len(matrix[0])

    first_row_zero = False
    for col in range(WIDTH):
        if matrix[0][col] == 0:
            first_row_zero = True

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if matrix[row][col] == 0:
                matrix[0][col] = 0

    for row in range(1, HEIGHT):
        row_contains_zero = False
        for col in range(WIDTH):
            if matrix[row][col] == 0:
                row_contains_zero = True
                break
        for col in range(WIDTH):
            if row_contains_zero or matrix[0][col] == 0:
                matrix[row][col] = 0
    
    if first_row_zero:
        for col in range(WIDTH):
            matrix[0][col] = 0

    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix1(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()