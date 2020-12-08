from collections import deque

class Solution:
    def generateParenthesis(self, n):
        res = []
        q = deque()
        q.append({'s': '', 'open': 0, 'close': 0})
        while q:
            cur = q.popleft()
            if cur['open'] == n and cur['close'] == n:
                res.append(cur['s'])
            else:
                if cur['open'] < n:
                    new_s = cur['s'] + '('
                    new_open_c = cur['open'] + 1
                    q.append({'s': new_s, 
                              'open': new_open_c, 
                              'close': cur['close']})
                if cur['open'] > cur['close']:
                    new_s = cur['s'] + ')'
                    new_close_c = cur['close'] + 1
                    q.append({'s': new_s,
                             'open': cur['open'],
                             'close': new_close_c})  
        return res

class Solution2:
    def generateParenthesis(self, n):
        self.res = []
        self.n = n
        self.backtrack('', 0, 0)
        return self.res
    
    def backtrack(self, s, left, right):
        if len(s) == self.n * 2:
            self.res.append(s)
            return
        if left < self.n:
            self.backtrack(s + '(', left+1, right)
        if left > right:
            self.backtrack(s + ')', left, right+1)