class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num): return "0"

        i = 0
        while (k > 0):
            if i > 0:
                i -= 1
            while (i < len(num)-1) and (num[i] <= num[i+1]):
                i += 1
            num = num[:i] +  num[i+1:]
            k -= 1

        # edge: leading zeros; "00032" -> "32"
        num = num.lstrip("0")

        # edge: empty num
        if len(num) == 0:
            return "0"

        return num