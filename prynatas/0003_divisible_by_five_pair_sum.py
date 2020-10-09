def divisible_by_five_pair_sum(array):
    results = []

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if (array[i] + array[j]) % 5 == 0:
                results.append([i, j])

    return results

print(divisible_by_five_pair_sum([1, 5, 2, 0, 4])) 
# => [ [ 0, 4 ], [ 1, 3 ] ]
print(divisible_by_five_pair_sum([13, 22, 8, -3, 12])) 
# => [[ 0, 1 ], [ 0, 3 ], [ 0, 4 ], [ 1, 2 ], [ 2, 3 ], [ 2, 4 ]]