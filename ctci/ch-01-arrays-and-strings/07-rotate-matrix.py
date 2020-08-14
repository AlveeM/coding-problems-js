import unittest

# top = matrix[i][j]
# left = matrix[n - 1 - j][i]
# bottom = matrix[n - i - 1][n - j - 1]
# right = matrix[j][n - i - 1]

# Method 1: 4-way swap at each layer of the matrix (outer to inner)
# TC: O(n^2)
# SC: O(1)
def rotate_matrix(matrix):
    i = 0
    j = 0
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            top_temp = matrix[i][j]
            
            # top = left (left -> top)
            matrix[i][j] = matrix[n - 1 - j][i]

            # left = bottom (bottom -> left)
            matrix[n - 1 - j][i] = matrix[n - i - 1][n - j - 1]

            # bottom = right (right -> bottom)
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

            # right = top_temp (top -> right)
            matrix[j][n - i - 1] = top_temp

    return matrix

# Method 2: transpose matrix and then reverse each row
# TC: O(n^2)
# SC: O(1)
def rotate_matrix2(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        start = 0
        end = n - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([                       
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]),
        ([
            [ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12],
            [13, 14, 15, 16]
        ], [
            [13,  9,  5,  1],
            [14, 10,  6,  2],
            [15, 11,  7,  3],
            [16, 12,  8,  4]
        ]),
        ([
            [ 1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]),
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
