# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:
  def lengthOfLongestSubstringKDistinct(self, s, k):
    max_len = 0
    char_freq = {}
    window_start = 0

    for window_end in range(len(s)):
      end_char = s[window_end]

      if end_char not in char_freq:
        char_freq[end_char] = 0
      char_freq[end_char] += 1

      while len(char_freq) > k:
        start_char = s[window_start]
        char_freq[start_char] -= 1
        if char_freq[start_char] == 0:
          del char_freq[start_char]
        window_start += 1
      
      max_len = max(max_len, window_end - window_start + 1)

    return max_len

# s = "eceba"
# k = 2
# print(lengthOfLongestSubstringKDistinct(s, k)) # 3

# s = "aa"
# k = 1
# print(lengthOfLongestSubstringKDistinct(s, k)) # 2