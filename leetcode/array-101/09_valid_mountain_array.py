from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[0] >= A[1]:
            return False
			
        downhill = False
        
        for i in range(1,len(A)):
            if not downhill:
                if A[i] <= A[i-1]:
                    downhill = True
            if downhill:
                if A[i] >= A[i-1]:
                    return False
        
        return downhill

# A1 = [0, 2, 3, 4, 5, 2, 1, 0] # True
# A2 = [0, 2, 3, 3, 5, 2, 1, 0] # False
# A3 = [0, 3, 2, 1] # True
# A4 = [3, 5, 5] # False
# A5 = [0, 3, 2, 1] # True

# test_arr = [A1, A2, A3, A4, A5]
# validMountainArray = Solution().validMountainArray

# for arr in test_arr:
#     print(validMountainArray(arr))