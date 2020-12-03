import random

class Solution:

    def __init__(self, nums):
        self.original = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        arr = self.original.copy()
        for i in range(len(arr)):
            swap_idx = random.randrange(i, len(arr))
            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
        return arr