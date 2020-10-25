from collections import Counter

def makeAnagram(a, b):
    min_dels = 0
    a_freq = [0] * 26
    b_freq = [0] * 26
    
    for char in a:
        a_freq[ord(char)-97] += 1
    
    for char in b:
        b_freq[ord(char)-97] += 1

    for i in range(26):
        min_dels += abs(a_freq[i] - b_freq[i])
    
    return min_dels

def makeAnagram2(a, b):
    a_dict = Counter(a)
    b_dict = Counter(b)
    a_dict.subtract(b_dict)
    return sum(abs(val) for val in a_dict.values())

a = "cde"
b = "abc"

print(makeAnagram(a, b)) # cd, dc