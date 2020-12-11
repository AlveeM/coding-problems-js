class Solution:
    def search(self, reader, target):
      l = 0
      r = 1

      while reader.get(r) < target:
        r *= 2
      l = r // 2

      while l <= r:
        mid = (l + r) // 2
        val = reader.get(mid)
        if val == target:
          return mid
        elif val > target:
          r = mid - 1
        else:
          l = mid + 1

      return -1