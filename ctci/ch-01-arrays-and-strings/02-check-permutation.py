import unittest

# TC: O(n log n)
def check_permutation(str1, str2):
    if len(str1) != len(str2): return False 

    str1_sorted = ''.join(sorted(str1))
    str2_sorted = ''.join(sorted(str2))

    return str1_sorted == str2_sorted

# TC: O(n)
# def check_permutation(str1, str2):
#     if len(str1) != len(str2): return False

#     counter = {}

#     for char in str1:
#         counter[char] = counter.get(char, 0) + 1
#     for char in str2:
#         if char not in counter or counter[char] == 0:
#             return False
#         counter[char] -= 1

#     return True

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()