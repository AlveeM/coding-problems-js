# Method 1: do a binary search to find the possible row and do a binary search on that row
class Solution:
    def searchMatrix(self, matrix, target):
        r = len(matrix)
        if r == 0: return False
        c = len(matrix[0])
        if c == 0: return False
        
        r1 = 0
        r2 = r - 1
        while r1 <= r2:
            mid = r1 + (r2 - r1) // 2
            if matrix[mid][-1] < target:
                r1 = mid + 1
            elif matrix[mid][0] > target:
                r2 = mid - 1
            else:
                return self.binarySearch(matrix[mid], target)
            
        return False
        
    def binarySearch(self, arr, target):
        l = 0
        r = len(arr) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return True
            elif target > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
                
        return False

# Method 2: think of the matrix as a 1D array
# for i in range(m*n): r = i // n, c = i % n; m -> no. of rows, n -> no. of cols
# n * m matrix convert to an array => matrix[x][y] => a[x * m + y]
# an array convert to n * m matrix => a[x] =>matrix[x / m][x % m];
class Solution2:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False
        
        low = 0
        high = (m * n) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            r = mid // n
            c = mid % n
            num = matrix[r][c]
            
            if target == num:
                return True
            elif target > num:
                low = mid + 1
            else:
                high = mid - 1
                
        return False