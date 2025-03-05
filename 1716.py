class Solution(object):
    def totalMoney(self, n):
        sum_vals = 0
        increment = 0
        weeks = 0
        for i in range(1,n+1):
            increment += 1
            if increment == 8+weeks:
                weeks += 1
                increment = 1+weeks
            sum_vals += increment
        return sum_vals
        
