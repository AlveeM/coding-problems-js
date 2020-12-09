class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        opens = ('(', '{', '[')
        matches = (('(', ')'), ('{', '}'), ('[', ']'))
        
        for paren in s:
            if paren in opens:
                stack.append(paren)
            else:
                if stack:
                    last_open = stack.pop()
                    match = (last_open, paren)
                    if match not in matches:
                        return False
                else:
                    return False
                
        return len(stack) == 0