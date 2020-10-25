def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1, -1, -1):
        # check if current is in the wrong position
        if q[i] != i + 1:
            # check if the correct element is in the previous position
            if (i-1 >= 0) and (q[i-1] == i + 1):
                # move the elements in the correct positions
                q[i-1] = q[i]
                q[i] = i + 1

                bribes += 1
            # check if the corrent element is two positions behind
            elif (i-2 >= 0 ) and (q[i-2] == i + 1):
                # move the elements in the correct positions
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = i + 1

                bribes += 2
            else:
                print("Too chaotic")
                return
    print(bribes)

arr1 = [2, 1, 5, 3, 4]
arr2 = [2, 5, 1, 3, 4]

print(minimumBribes(arr1))
print(minimumBribes(arr2))