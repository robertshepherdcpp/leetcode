class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        if len(s) == 0: return 0
        for l in range(0, len(s)):
            curr = ""
            for r in range(l, len(s)):
                if s[r] not in curr:
                    curr += str(s[r])
                    max_len = max(max_len, len(curr))
                else:
                    break
        return max_len


        
