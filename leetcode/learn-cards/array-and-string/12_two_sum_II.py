class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            cur = numbers[left] + numbers[right]
            
            if cur == target:
                return (left+1, right+1)
            if cur > target:
                right -= 1
            if cur < target:
                left += 1