class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i in range(len(nums)):
            max_reach = max(nums[i] + i, max_reach)
            if max_reach == i:
                break
        
        return max_reach >= len(nums) - 1