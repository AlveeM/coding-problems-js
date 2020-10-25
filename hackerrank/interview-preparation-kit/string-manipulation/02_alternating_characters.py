def alternatingCharacters(s):
    min_dels = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            i += 1
            min_dels += 1
    return min_dels