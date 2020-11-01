from collections import Counter

# using dict
class Solution1:
    def singleNumber(self, nums):
        nums_dict = Counter(nums)
        
        for num, count in nums_dict.items():
            if count == 1:
                return num

# using set
class Solution2:
    def singleNumber(self, nums):
        nums_set = set()
        
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                nums_set.add(num)
                
        return nums_set.pop()

# using XOR
class Solution3:
    def singleNumber(self, nums):
        res = 0
        
        for num in nums:
            res = res ^ num

        return res

nums = [2, 2, 1]
print(Solution3().singleNumber(nums))