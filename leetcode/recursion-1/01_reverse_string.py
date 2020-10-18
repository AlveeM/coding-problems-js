class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(l_idx, r_idx):
            if l_idx >= r_idx:
                return
            
            s[l_idx], s[r_idx] = s[r_idx], s[l_idx]
            return helper(l_idx + 1, r_idx - 1)
        
        helper(0, len(s)-1)