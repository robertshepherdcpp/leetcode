class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return nums
        f,l=0,0
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[l] == 1:
                l += 1
            elif nums[i] - nums[l] >= 2:
                if f == l:
                    res.append(str(nums[f]))
                else:
                    res.append(str(nums[f]) + "->" + str(nums[l]))
                f=l=i
        if f == l:
            res.append(str(nums[f]))
        else:
            res.append(str(nums[f]) + "->" + str(nums[l]))
        return res

        
