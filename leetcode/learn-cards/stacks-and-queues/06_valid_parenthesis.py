class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for br in s:
            if br == '(' or br == '{' or br == '[':
                stack.append(br)
            else:
                if stack:
                    br_s = stack.pop()
                    if ((br_s == '(' and br != ')') 
                            or (br_s == '{' and br != '}') 
                            or (br_s == '[' and br != ']')):
                        return False
                else:
                    return False
                
        return len(stack) == 0

class Solution2:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        opening = ('(', '{', '[')
        matches = (('(', ')'), ('{', '}'), ('[', ']'))
        
        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if len(stack) != 0:
                    last_open = stack.pop()
                    if (last_open, paren) not in matches:
                        return False
                else:
                    return False
                
        return len(stack) == 0