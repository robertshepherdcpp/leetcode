class Solution(object):
    def isHappy(self, n):
        sum_arr = 0
        visit = set()
        while sum_arr != 1:
            arr = [i for i in str(n)]
            sum_arr = sum(int(i)**2 for i in arr)
            n = sum_arr
            if sum_arr in visit: 
                return False
            else:
                visit.add(sum_arr)
        return True
        
