class Solution(object):
    def searchInsert(self, nums, target):
        closest = len(nums)-1
        if len(nums) == 1:
            return 1 if nums[0] < target else 0
        for i in range(len(nums)):
            if  abs(target - nums[i]) < abs(target - nums[closest]):
                closest = i
            if nums[i] == target:
                return i
        return closest+1 if nums[closest] < target else closest
        # if nums[closest] < target:
        #     return closest+1
        # else:
        #     if closest == -1:
        #         return 0
        #     else:
        #         return closest
        
