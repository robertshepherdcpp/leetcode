def XORSum(nums):
    count = 0
    for i in nums:
        count ^= i
    return count

class Solution(object):
    def subsetXORSum(self, nums):
        count = 0
        unique_perms = []
        for i in range(1, len(nums)+1):
            unique_perms += combinations(nums, i)
        for i in unique_perms:
            count += XORSum(i)
        return count
        
