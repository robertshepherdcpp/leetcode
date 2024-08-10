class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if(i != j and nums[i] + nums[j] < target):
                    count += 1
        return int(count / 2)
