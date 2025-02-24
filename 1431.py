class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        arr = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                arr[i] = True
        return arr
        
