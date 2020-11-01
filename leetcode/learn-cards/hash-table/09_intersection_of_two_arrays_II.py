from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        seen = Counter(nums1)
        res = []

        for num in nums2:
            if seen[num] > 0:
                res.append(num)
                seen[num] -= 1

        return res