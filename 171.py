class Solution(object):
    def titleToNumber(self, title):
        sum_ = 0
        mult = 1
        for i in range(len(title)-1, -1, -1):
            sum_ += mult * (ord(title[i]) - ord("A") + 1)
            mult *= 26
        return sum_
