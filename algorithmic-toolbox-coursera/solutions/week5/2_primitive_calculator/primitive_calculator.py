import sys

def optimal_sequence(n):
    min_ops = [0] * (n+1)
    for i in range(1, n+1):
        min_ops[i] = min_ops[i - 1] + 1
        if i % 2 == 0:
            min_ops[i] = min(1 + min_ops[i // 2], min_ops[i])
        if i % 3 == 0:
            min_ops[i] = min(1 + min_ops[i // 3], min_ops[i])

    sequence = []
    while n > 1:
        sequence.append(n)
        if min_ops[n - 1] == min_ops[n] - 1:
            n = n - 1
        elif (n % 2 == 0) and (min_ops[n // 2] == min_ops[n] - 1):
            n = n // 2
        elif (n % 3 == 0) and (min_ops[n // 3] == min_ops[n] - 1):
            n = n // 3

    sequence.append(1)
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')