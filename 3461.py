class Solution(object):
    def hasSameDigits(self, s):
        string = ""
        # while len(arr) != 2:
        #     s = ''.join(str(i) for i in arr)
        #     arr = []
        while len(s) != 2:
            for i in range(len(s)-1):
                string += str((int(s[i])+int(s[i+1]))%10)
            s,string=string,""
        print(s)
        return s[0] == s[1]
        
