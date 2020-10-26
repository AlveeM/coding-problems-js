from collections import Counter

def sherlockAndAnagrams(s):
    n = len(s)
    sub_strings = {}
    for i in range(1, n):
        for j in range(n-i+1):
            sub_string = ''.join(sorted(s[j:j+i]))
            sub_strings[sub_string] = sub_strings.get(sub_string, 0) + 1

    # pair count for each key in sub_strings = (val * (val - 1)) / 2
    return sum((val * (val - 1) // 2) for val in sub_strings.values())

s = "abba"
print(sherlockAndAnagrams(s))