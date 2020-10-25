def hourglassSum(arr):
    max_sum = float("-inf")
    for i in range(4):
        for j in range(1, 5):
            hourglass_sum = (arr[i][j-1]
                            + arr[i][j]
                            + arr[i][j+1]
                            + arr[i+1][j]
                            + arr[i+2][j-1]
                            + arr[i+2][j]
                            + arr[i+2][j+1])
            max_sum = max(hourglass_sum, max_sum)
    return max_sum

arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

print(hourglassSum(arr))