from collections import Counter

class Solution:
    def singleNumber(self, nums):
        counts = Counter(nums)
        for num, count in counts.items():
            if count == 1:
                return num

class Solution2:
    def singleNumber(self, nums):
        num_set = set()
        
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
                
        return num_set.pop()

