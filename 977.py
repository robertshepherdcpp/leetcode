class Solution(object):
    def sortedSquares(self, nums):
        copy = []
        result = []
        for i in nums:
            copy.append(abs(i))
        copy.sort()
        for i in copy:
            result.append(i * i)
        return result
