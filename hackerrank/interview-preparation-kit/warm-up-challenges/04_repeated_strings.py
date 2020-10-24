def repeatedString(s, n):
    count_a = 0

    for letter in s:
        if letter == 'a': count_a += 1

    count_a = count_a * (n // len(s))
    
    for i in range(n % len(s)):
        if s[i] == 'a': count_a += 1

    return count_a