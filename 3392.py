class Solution(object):
    def countSubarrays(self, nums):
        l,r=0,2
        count = 0
        while r != len(nums):
            if float(nums[l] + nums[r]) == (float(nums[l+1])/2):
                count += 1
            l,r=l+1,r+1
        return count
        
