# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n 

    second_last_num = 0
    last_num = 1

    for _ in range(1, n):
        # temp = last_num
        # last_num = second_last_num + last_num
        # second_last_num = temp
        second_last_num, last_num = last_num, second_last_num + last_num
    
    return last_num

n = int(input())
print(calc_fib(n))
