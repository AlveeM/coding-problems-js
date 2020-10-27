def arrayManipulation(n, queries):
    res = [0] * (n + 1)
    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        res[a] += k
        res[b] -= k

    max_sum = 0
    cur_sum = 0
    for num in res:
        cur_sum += num
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum

n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
print(arrayManipulation(n, queries))

n2 = 5
queries2 = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
print(arrayManipulation(n2, queries2))