from collections import Counter

def isValid(s):
    s_dict = Counter(s)
    count_dict = Counter(s_dict.values())
    count_dict_keys = count_dict.keys()
    max_key = max(count_dict_keys)
    min_key = min(count_dict_keys)

    if len(s) == 1 or max_key - min_key == 0:
        return "YES"
    elif len(count_dict_keys) == 2:
        if (max_key - min_key == 1 and count_dict[max_key] == 1) or (min_key == 1 and count_dict[min_key] == 1):
            return "YES"
    
    return "NO"

s = "aabbcd"
print(isValid(s))