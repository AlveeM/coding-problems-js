def isBadVersion(version):
  return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
                
        return l