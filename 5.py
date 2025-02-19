class Solution(object):
    def longestPalindrome(self, s):
        max_str = ""
        for l in range(0, len(s)):
            curr = ""
            for r in range(l+len(max_str), len(s)):
                if s[l:r+1] == s[l:r+1][::-1]:
                    max_str = s[l:r+1]
        return max_str
