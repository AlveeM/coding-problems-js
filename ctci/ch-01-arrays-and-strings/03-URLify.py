import unittest

# Method 1: in-place replacement
# TC: O(n)
# SC: O(1)
def urlify(str_list, true_str_len):
    new_idx = len(str_list)

    for char in reversed(str_list[:true_str_len]):
        if char == ' ':
            str_list[new_idx - 3:new_idx] = '%20'
            new_idx -= 3
        else:
            str_list[new_idx - 1] = char
            new_idx -= 1
    
    return str_list

# Method 2: copying the string while replacing spaces
# TC: O(n) 
# SC: O(n)
# def urlify(str_list, true_str_len):
#     new_str = []
#     for i in range(true_str_len):
#         if str_list[i] == ' ':
#             new_str.extend(['%', '2', '0'])
#         else:
#             new_str.append(str_list[i])

#     return new_str

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()