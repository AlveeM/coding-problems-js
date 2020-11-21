from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        small = []
        large = []
        
        if len(nums1) < len(nums2):
            small = nums1
            large = nums2
        else:
            small = nums2
            large = nums1
            
        counts = Counter(small)
        
        res = []
        for num in large:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        
        return res
            
        