class Solution(object):
    def reverseWords(self, s):
        def spaced(i):
            return i + " "
        # s = s.replace("  ", "")
        for i in range(len(s)):
            if s[i] != ' ':
                s = s[i:]
                break
        string = ""
        last_idx = 0
        #for i in range(len(s)):
        i = 0
        while i < len(s):
            if s[i] != " " and (i - last_idx) > 2:
                s.replace(" " * (i - last_idx - 2), "", 1)
                i -= (i - last_idx - 1)
                last_idx = i
            elif s[i] == " ":
                i += 1
            elif s[i] != " ":
                i += 1
                last_idx = i
                


        arr = []
        while s.find(" ") != -1:
            arr.append(s[: s.find(" ")])
            s = s[s.find(" ")+1:]
        arr.append(s)
        arr = [i for i in arr if i != '']
        string = ''.join(spaced(i) for i in arr[::-1])
        return string[:-1]
