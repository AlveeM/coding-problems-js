def jumpingOnClouds(c):
    i = 0
    steps = 0
    while i < len(c) - 2:
        if c[i+2] == 1:
            i += 1
        else:
            i += 2

        steps += 1
    
    if i == len(c) - 2:
        steps += 1

    return steps

# def jumpingOnClouds(c):
#     i = 0
#     steps = 0
#     while i < len(c)-1:
#         if c[i] == 0: i += 1
#         i += 1
#         steps += 1
#     return steps
