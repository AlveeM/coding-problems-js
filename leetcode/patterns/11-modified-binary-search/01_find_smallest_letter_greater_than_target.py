class Solution:
    def nextGreatestLetter(self, letters, target):
        l = 0
        r = len(letters) - 1
        
        if letters[0] > target or letters[-1] <= target:
            return letters[0]
        
        while l < r:
            mid = (l + r) // 2
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1
                
        return letters[l]