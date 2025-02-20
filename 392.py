class Solution(object):
    def isSubsequence(self, s, t):
        str_list = list(s)
        for i in t:
            if str_list and i == str_list[0]:
                str_list.pop(0)
            elif not str_list:
                break
        return len(str_list) == 0
        
