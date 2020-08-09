# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max_value(i, j):
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i, j):
        a = evalt(d_max[i][k], d_max[k+1][j], ops[k])
        b = evalt(d_max[i][k], d_min[k+1][j], ops[k])
        c = evalt(d_min[i][k], d_max[k+1][j], ops[k])
        d = evalt(d_min[i][k], d_min[k+1][j], ops[k])
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d) 
    return min_val, max_val

def get_maximum_value(dataset):
    for i in range(len(nums)):
        d_max[i][i] = nums[i]
        d_min[i][i] = nums[i]

    for s in range(len(nums)):
        for i in range(len(nums) - s - 1):
            j = i + s + 1
            min_val, max_val = min_max_value(i, j)
            d_min[i][j] = min_val
            d_max[i][j] = max_val 
    return 0


if __name__ == "__main__":
    user_input = input()
    nums = list(map(int, user_input[::2]))
    ops = list(user_input[1::2])
    d_min = [[0 for j in range(len(nums))] for i in range(len(nums))]
    d_max = [[0 for j in range(len(nums))] for i in range(len(nums))]
    get_maximum_value(user_input)
    print(d_max[0][len(nums) - 1])
