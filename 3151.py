class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if (nums[i] + nums[i+1]) % 2 != 1:
                return False
        return True

        
