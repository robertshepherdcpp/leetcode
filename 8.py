class Solution:
    def myAtoi(self, s):
        dictionary = {'1':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        # s = s.replace(" ", "")
        for i in range(len(s)):
            if s[i] != ' ':
                s = s[i:]
                break
        
        if s == "+" or s == "-":
            return 0
        negative = False
        if s == "":
            return 0
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            negative = False
            s = s[1:]
        for i in range(len(s)):
            if not s[i].isnumeric():
                s = s[:i]
                break
        for i in range(len(s)):
            if s[i] != 0:
                if i != 0:
                    s = s[i-1:]
                    break
        res = 0
        mult = 1
        for i in reversed(s):
            res += dictionary[i] * mult
            mult *= 10
        if negative:
            res *= -1
        if res > (2**31 - 1):
            res = 2**31 - 1
        elif res < (-2**31):
            res = -2**31
        return res
