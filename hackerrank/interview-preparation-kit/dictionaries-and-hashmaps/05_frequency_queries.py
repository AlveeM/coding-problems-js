def freqQuery(queries):
    nums = {}
    counts = {}
    res = []

    for op, val in queries:
        if op == 1:
            if val in nums:
                old_count = nums[val]
                counts[old_count] -= 1
                nums[val] += 1
                new_count = nums[val]
                counts[new_count] = counts.get(new_count, 0) + 1
            else:
                nums[val] = 1
                counts[1] = counts.get(1, 0) + 1
        elif op == 2:
            if val in nums and nums[val] > 0:
                old_count = nums[val]
                counts[old_count] -= 1
                nums[val] -= 1
                new_count = nums[val]
                counts[new_count] = counts.get(new_count, 0) + 1
        else:
            if counts.get(val, 0) >= 1:
                res.append(1)
            else:
                res.append(0)

    return res

queries = [
    [1, 5],
    [1, 6],
    [3, 2],
    [1, 10],
    [1, 10],
    [1, 6],
    [2, 5],
    [3, 2]
]

print(freqQuery(queries))

queries2 = [
    [1, 1],
    [2, 2],
    [3, 2],
    [1, 1],
    [1, 1],
    [2, 1],
    [3, 2]
]

print(freqQuery(queries2))