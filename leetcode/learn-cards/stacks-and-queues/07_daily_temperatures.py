# Method 1
class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        res = [0] * n
        stack = []
        
        for i in range(n-1, -1, -1):
            cur_temp = T[i]
            
            while stack:
                top_temp = T[stack[-1]]
                if top_temp > cur_temp:
                    res[i] = stack[-1] - i
                    break
                else:
                    stack.pop()
            
            stack.append(i)
                
        return res

# Method 2
class Solution2:
    def dailyTemperatures(self, T):
        res = [0] * len(T)
        stack = []
        
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
            
        return res