class Solution(object):
    def maximumCount(self, nums):
        odd = 0
        even = 0
        for i in nums:
            if i < 0:
                odd += 1
            elif i > 0:
                even += 1
        return max(odd, even)
