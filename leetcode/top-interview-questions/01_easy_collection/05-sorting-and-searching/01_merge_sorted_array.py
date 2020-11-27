class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            num1 = nums1[m - 1]
            num2 = nums2[n - 1]
            last_idx = m + n - 1
            
            if num1 > num2:
                nums1[last_idx] = num1
                m -= 1
            else:
                nums1[last_idx] = num2
                n -= 1
            
        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1