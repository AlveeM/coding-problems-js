ops = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b)
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in ops:
                num1 = stack.pop()
                num2 = stack.pop()
                res = ops[token](num2, num1)
                stack.append(res)
            else:
                stack.append(int(token))
                
        return stack[0]