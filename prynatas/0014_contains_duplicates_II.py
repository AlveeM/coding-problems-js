class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for idx, val in enumerate(nums):
            if val in seen and idx - seen[val] <= k:
                return True 
            seen[val] = idx
        return False

# space optimized with fixed-size set
class Solution2:
    def containsNearbyDuplicate(self, nums, k):
        seen = set()
        for idx, val in enumerate(nums):
            if val in seen:
                return True
            seen.add(val)
            if len(seen) > k:
                seen.remove(nums[idx-k])
        return False