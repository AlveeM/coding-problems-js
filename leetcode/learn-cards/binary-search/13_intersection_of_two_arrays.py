class Solution:
    def intersection(self, nums1, nums2):
        nums1_sorted = sorted(nums1)
        common = set()
        
        for num in nums2:
            if self.binarySearch(nums1_sorted, num):
                common.add(num)
        
        return list(common)
        
    def binarySearch(self, arr, target):
        l = 0
        r = len(arr) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return True
            elif target > arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
                
        return False