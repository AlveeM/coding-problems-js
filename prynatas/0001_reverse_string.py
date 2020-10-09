def reverseString(string):
    result_str = ""

    for i in range(len(string)-1, -1, -1):
        result_str += string[i]

    return result_str