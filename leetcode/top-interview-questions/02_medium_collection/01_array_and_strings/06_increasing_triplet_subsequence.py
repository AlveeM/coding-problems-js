class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        
        left_min = [float('inf')] * n
        left_min[0] = nums[0]
        right_max = [float('-inf')] * n
        right_max[-1] = nums[-1]
        
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], nums[i])
        
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
            
        for i in range(n):
            if left_min[i] < nums[i] < right_max[i]:
                return True
            
        return False

class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False