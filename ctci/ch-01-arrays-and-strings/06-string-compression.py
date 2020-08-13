import unittest

# TC: O(n)
# SC: O(n)
def string_compression(string):
    compressed_list = []
    counter = 0
    
    for i in range(len(string)):
        if string[i] != string[i - 1]:
            compressed_list.append(string[i-1] + str(counter))
            counter = 0
        counter += 1

    compressed_list.append(string[i-1] + str(counter))

    compressed_str = ''.join(compressed_list)
    if len(compressed_str) > len(string):
        return string
    
    return compressed_str

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
