class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.traverse(nums, [])
        return self.res
    
    def traverse(self, nums, path):
        if len(nums) == 0:
            self.res.append(path)
            return
        
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            new_path = path + [nums[i]]
            self.traverse(new_nums, new_path)

class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.visited = set()
        self.res = []
        self.backtrack(nums, [])
        return self.res
    
    def backtrack(self, nums, path):
        if len(nums) == len(path):
            self.res.append(path.copy())
            return
        
        for num in nums:
            if num not in self.visited:
                self.visited.add(num)
                self.backtrack(nums, path + [num])
                self.visited.remove(num)