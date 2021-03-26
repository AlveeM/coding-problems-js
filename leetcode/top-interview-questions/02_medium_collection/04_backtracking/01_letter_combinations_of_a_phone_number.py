class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        
        self.letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        self.digits = digits
        self.res = []
        self.backtrack(0, [])
        return self.res
    
    def backtrack(self, idx, path):
        if len(path) == len(self.digits):
            self.res.append(''.join(path))
            return
        
        letters = self.letters[self.digits[idx]]
        for letter in letters:
            path.append(letter)
            self.backtrack(idx + 1, path)
            path.pop()