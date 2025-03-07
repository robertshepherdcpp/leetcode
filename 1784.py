class Solution(object):
    def checkOnesSegment(self, s):
        idx = -1
        if "0" in s:
            idx = s.index("0")
        else:
            return True
        arr = s[idx:]
        return ("1" not in arr)
        
