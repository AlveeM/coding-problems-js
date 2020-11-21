class Solution:
    def searchRange(self, nums, target):
        res = [-1, -1]
        
        if not nums: return res
        if nums[0] > target or nums[-1] < target: return res
        
        first = self.binarySearch(nums, target, True)
        last = self.binarySearch(nums, target, False)
            
        return [first, last]
        
    def binarySearch(self, nums, target, first):
        idx = -1
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                idx = mid
                if first:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return idx

def binarySearchFirstElement(nums, target):
    idx = -1
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            idx = mid
            r = mid - 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return idx

def binarySearchLastElement(nums, target):
    idx = -1
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            idx = mid
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return idx

arr = [5,7,7,8,8,8,8,10]
print(binarySearchFirstElement(arr, 8))
print(binarySearchLastElement(arr, 8))