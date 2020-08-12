import unittest

# Method 1: compare string lengths and check if only one edit is required to make the strings same
# TC: O(n)
def one_away(str1, str2):
    if str1 == str2:
        return True

    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)
    elif abs(len(str1) - len(str2)) == 1:
        return one_insert_or_removal(str1, str2)
    return False

def one_edit_replace(str1, str2):
    edited = False
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            if edited:
                return False
            edited = True
    return True

def one_insert_or_removal(str1, str2):
    edited = False
    idx1, idx2 = 0, 0

    while idx1 < len(str1) and idx2 < len(str2):
        if str1[idx1] != str2[idx2]:
            if edited:
                return False
            
            if len(str1) > len(str2):
                idx1 += 1
            else:
                idx2 += 1

            edited = True
        else:
            idx1 += 1
            idx2 += 1
    
    return True

# Method 2: same approach as method 1 but without helper functions
# TC: O(n)
# def one_away(str1, str2):
#     if str1 == str2:
#         return True 

#     str1_len = len(str1)
#     str2_len = len(str2)

#     if abs(str1_len - str2_len) > 1:
#         return False

#     edit_count = 0
#     idx1, idx2 = 0, 0

#     while idx1 < str1_len and idx2 < str2_len:
#         if str1[idx1] != str2[idx2]:
#             if edit_count == 1:
#                 return False

#             if str1_len > str2_len:
#                 idx1 += 1
#             elif str1_len < str2_len:
#                 idx2 += 1
#             else:
#                 idx1 += 1
#                 idx2 += 1

#             edit_count += 1
#         else:
#             idx1 += 1
#             idx2 += 1

#     if idx1 < str1_len or idx2 < str2_len:
#         edit_count += 1 
    
#     return edit_count == 1

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()