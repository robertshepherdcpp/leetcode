class Solution(object):
    def applyOperations(self, nums):
        start = len(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        zero_count = nums.count(0)
        i=0
        while len(nums) != start-zero_count:
            if nums[i] == 0:
                nums.pop(i)
            else:
                i += 1
        return nums + [0] * (start-len(nums))
        
