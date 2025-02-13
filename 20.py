class Solution(object):
    def isValid(self, s):
        while s.find("()") != -1 or s.find("{}") != -1 or s.find("[]") != -1:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        if len(s) > 0:
            return False
        else:
            return True
