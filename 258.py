class Solution(object):
    def addDigits(self, num):
        sum_num = str(num)
        while len(sum_num) > 1:
            arr = []
            for i in sum_num:
                arr.append(int(i))
            sum_int = 0
            for i in arr:
                sum_int += i
            sum_num = str(sum_int)

        return int(sum_num)
        
