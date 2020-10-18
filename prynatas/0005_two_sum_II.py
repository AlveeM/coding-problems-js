from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(numbers) - 1
        
        while left_idx < right_idx:
            current_sum = numbers[left_idx] + numbers[right_idx]
            
            if target == current_sum:
                return [left_idx + 1, right_idx + 1]
            
            if target > current_sum:
                left_idx += 1
            else:
                right_idx -= 1