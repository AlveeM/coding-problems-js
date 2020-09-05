import unittest

# is_substring is provided
# TC: O(N*M) 
def is_substring(string, sub):
    return string.find(sub) != -1

# Method
# s1 = "waterbottle"
# s2 = "erbottlewat"
# x = "wat"
# y = "erbottle"
# s1 xy = "waterbottlewaterbottle"
# s2 = yx = "erbottlewat"
# xy + xy = x(yx)y  # yx is always a substring

def is_string_rotation(str1, str2):
    if len(str1) != len(str2):
        return False 
    return is_substring(str1 + str1, str2)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_is_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = is_string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
