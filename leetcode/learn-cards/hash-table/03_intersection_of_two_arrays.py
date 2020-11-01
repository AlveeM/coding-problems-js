class Solution:
    def intersection(self, nums1, nums2):
        res = set()
        seen = set(nums1)
        
        for num in nums2:
            if num in seen:
                res.add(num)
                
        return list(res)

class Solution2:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))