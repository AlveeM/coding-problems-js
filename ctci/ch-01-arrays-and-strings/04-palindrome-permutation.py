import re, unittest

# Method 1: count characters and check if two or more counts are odd
# TC: O(n)
# SC: O(n)
def pal_perm(phrase):
    counter = {}
    phrase_cleaned = re.sub(r'\W', '', phrase.lower())
    odd_count = 0

    for char in phrase_cleaned:
        counter[char] = counter.get(char, 0) + 1

    for char, count in counter.items():
        if count % 2 != 0:
            odd_count += 1

        if odd_count > 1:
            return False

    return True

# Method 2: check odd count while iterating over the string for the first time
# TC: O(n)
# SC: O(n)
def pal_perm_2(phrase):
    counter = {}
    phrase_cleaned = re.sub(r'\W', '', phrase.lower())
    odd_count = 0

    for char in phrase_cleaned:
        counter[char] = counter.get(char, 0) + 1
        if counter[char] % 2 != 0:
            odd_count += 1
        else:
            odd_count -= 1

    if odd_count > 1:
        return False
    else:
        return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
