class Solution(object):
    def maxAdjacentDistance(self, nums):
        max_num = 0
        for i in range(len(nums)-1):
            max_num = max(max_num, abs(nums[i]-nums[i+1]))
        max_num = max(max_num, abs(nums[0]-nums[-1]))
        return max_num
        