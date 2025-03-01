class Solution(object):
    def applyOperations(self, nums):
        start = len(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        vals = []
        zeros = []
        for i in nums:
            if i == 0:
                zeros.append(0)
            else:
                vals.append(i)
        return vals + zeros
        
