class Solution:
    def evalRPN(self, tokens):
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        stack = []
        
        for char in tokens:
            if char in ops:
                num1 = stack.pop()
                num2 = stack.pop()
                res = ops[char](num2, num1)
                stack.append(res)
            else:
                stack.append(int(char))
        
        return stack[0]