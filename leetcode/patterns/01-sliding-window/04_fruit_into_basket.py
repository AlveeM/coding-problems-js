# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, tree):
        max_len = 0
        fruits = {}
        window_start = 0
        
        for window_end in range(len(tree)):
            fruit_end = tree[window_end]
            
            if fruit_end not in fruits:
                fruits[fruit_end] = 0
            fruits[fruit_end] += 1
            
            while len(fruits) > 2:
                fruit_start = tree[window_start]
                fruits[fruit_start] -= 1
                
                if fruits[fruit_start] == 0:
                    del fruits[fruit_start]
                    
                window_start += 1
                
            max_len = max(max_len, window_end - window_start + 1)
            
        return max_len