class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConZeros = 0
        left = 0
        flips = 1
        zeros = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
                
            while zeros > flips:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            maxConZeros = max(right - left + 1, maxConZeros)
        
        return maxConZeros