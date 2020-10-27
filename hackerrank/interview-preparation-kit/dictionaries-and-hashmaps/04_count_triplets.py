from collections import Counter

def countTriplets(arr, r):
    before = {}
    after = Counter(arr)
    count = 0

    for num in arr:
        after[num] -= 1

        l_num = num // r
        r_num = num * r
        if l_num in before and num % r == 0 and r_num in after:
            count += before[l_num] * after[r_num]

        before[num] = before.get(num, 0) + 1
    
    return count


arr = [1, 2, 2, 4]
r = 2
print(countTriplets(arr, r)) # 2

arr2 = [1, 3, 9, 9, 27, 81]
r2 = 3
print(countTriplets(arr2, r2)) # 6

arr3 = [3, 9, 9, 9, 27]
r3 = 3
print(countTriplets(arr3, r3)) # 3