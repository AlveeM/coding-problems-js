class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        
        for _ in range(n-1):
            count = 1
            sub_str = []
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    sub_str.append(str(count))
                    sub_str.append(s[i-1])
                    count = 1
            sub_str.append(str(count))
            sub_str.append(s[-1])
            s = ''.join(sub_str)
        
        return s