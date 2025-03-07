class Solution(object):
    def checkOnesSegment(self, s):
        return ''.join(str(i) for i in sorted([int(i) for i in s])) == s or ''.join(str(i) for i in sorted(s)[::-1]) == s
        
