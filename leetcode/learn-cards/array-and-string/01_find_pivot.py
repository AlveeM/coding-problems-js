class Solution:
    def pivotIndex(self, nums):
        SumLeft = 0
        SumRight = sum(nums)
        for i in range(len(nums)):
            SumRight -= nums[i]
            if SumLeft == SumRight:
                return i
            SumLeft += nums[i]
        return -1