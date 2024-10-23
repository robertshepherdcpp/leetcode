class Solution(object):
    def maxSubArray(self, nums):
        highest = nums[0]
        current_sum = 0
        if len(nums) == 1:
            return nums[0]
        all_negatives = True
        for i in nums:
            if i > 0:
                all_negatives = False
        if all_negatives:
            return max(nums)
        for i in nums:
            current_sum += i
            if current_sum < 0:
                current_sum = 0
            if current_sum > highest:
                highest = current_sum
        return highest
            
