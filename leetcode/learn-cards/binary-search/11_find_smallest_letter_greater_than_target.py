class Solution:
    def nextGreatestLetter(self, letters, target):
        l = 0
        r = len(letters) - 1
        
        if letters[l] > target or letters[r] <= target:
            return letters[0]
        
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
                
        return letters[l]