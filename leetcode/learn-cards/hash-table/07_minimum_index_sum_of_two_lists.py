class Solution1:
    def findRestaurant(self, list1, list2):
        res = []
        l1_map = {val: idx for idx, val in enumerate(list1)}
        
        min_idx = float('inf')
        for idx, name in enumerate(list2):
            if name in l1_map:
                idx_sum = l1_map[name] + idx
                if idx_sum < min_idx:
                    min_idx = idx_sum
                    res = [name]
                elif idx_sum == min_idx:
                    res.append(name)
                
        return res

# less optimized version for reference (requires extra iteration and extra space for common)
# class Solution2:
#     def findRestaurant(self, list1, list2):
#         res = []
#         l1_map = {}
#         common = {}
        
#         for idx, name in enumerate(list1):
#             l1_map[name] = idx
        
#         min_idx = float('inf')
#         for idx, name in enumerate(list2):
#             if name in l1_map:
#                 idx_sum = l1_map[name] + idx
#                 common[name] = idx_sum
#                 if idx_sum < min_idx:
#                     min_idx = idx_sum
                    
#         for name, idx_sum in common.items():
#             if idx_sum == min_idx:
#                 res.append(name)
                
#         return res
        
        