class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        smallest_diff = float('inf')
        
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                cur_diff = target - cur_sum
                
                if cur_diff == 0:
                    return cur_sum
                elif cur_diff > 0:
                    l += 1
                else:
                    r -= 1
                    
                if abs(cur_diff) < abs(smallest_diff):
                    smallest_diff = cur_diff
                    
        return target - smallest_diff

class Solution2:
    def threeSumClosest(self, nums, target):
        nums.sort()
        cur_closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                old_diff = abs(cur_closest_sum - target)
                new_diff = abs(cur_sum - target)

                if new_diff < old_diff:
                    cur_closest_sum = cur_sum

                if cur_sum > target:
                    r -= 1
                elif cur_sum < target:
                    l += 1
                else:
                    return cur_closest_sum
                
        return cur_closest_sum