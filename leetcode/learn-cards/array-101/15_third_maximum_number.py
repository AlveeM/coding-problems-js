class Solution:
    def thirdMax(self, nums):
        maximum = nums[0]
        second_max = float('-inf')
        third_max = float('-inf')
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num > maximum:
                third_max = second_max
                second_max = maximum
                maximum = num
            elif num > second_max and num < maximum:
                third_max = second_max
                second_max = num
            elif num > third_max and num < second_max:
                third_max = num
                
        if third_max == float('-inf'): return maximum
        return third_max