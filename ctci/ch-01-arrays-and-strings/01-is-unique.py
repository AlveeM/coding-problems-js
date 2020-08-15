import unittest

# TC: O(n)
# SC: O(1)
def is_unique(string):
    # character set is in ASCII (128 characters)
    if len(string) > 128:
        return False

    char_list = [False for _ in range(128)]
    for char in string:
        char_idx = ord(char)
        if char_list[char_idx]:
            return False
        char_list[char_idx] = True

    return True

# TC: O(n)
# SC: O(n)
# def is_unique(string):
#     char_dict = {}
    
#     for char in string:
#         char_dict[char] = char_dict.get(char, 0) + 1
    
#     for key in char_dict:
#         if char_dict[key] > 1:
#             return False

#     return True

# TC: O(n)
# SC: O(n)
# def is_unique(string):
#     seen = set()

#     for char in string:
#         if char in seen:
#             return False
#         else:
#             seen.add(char)
    
#     return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_is_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()