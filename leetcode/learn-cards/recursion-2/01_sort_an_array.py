class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        return self.merge(left, right)
        
    def merge(self, arr1, arr2):
        res = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        res.extend(arr1[i:])
        res.extend(arr2[j:])
            
        return res