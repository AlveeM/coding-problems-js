from typing import List

# Recursive
def reverse_string(string):
    l = len(string)
    if l < 2:
        return string

    return reverse_string(string[l//2:]) + reverse_string(string[0:l//2])

# Recursive - in-place modification
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(l_idx, r_idx):
            if l_idx >= r_idx:
                return
            
            s[l_idx], s[r_idx] = s[r_idx], s[l_idx]
            return helper(l_idx + 1, r_idx - 1)
        
        helper(0, len(s)-1)

# Two Pointer
def reverse_string_2(string):
    l_idx = 0
    r_idx = len(string) - 1

    while l_idx < r_idx:
        string[l_idx], string[r_idx] = string[r_idx], string[l_idx]
        l_idx += 1
        r_idx -= 1