class Solution(object):
    def isValid(self, s):
        arr = []
        opening = "({["
        closing = ")}]"
        for i in range(len(s)):
            if s[i] in opening:
                arr.append(s[i])
            elif s[i] in closing:
                if not arr:
                    return False
                if arr[-1] == opening[closing.index(s[i])]:
                    arr.pop()
                else:
                    return False
        return True if len(arr) == 0 else False

        
