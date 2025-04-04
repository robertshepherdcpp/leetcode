class Solution(object):
    def distinctAverages(self, nums):
        hashmap = {}
        while len(nums) > 0:
            low = min(nums)
            nums.pop(nums.index(low))
            if nums:
                high = max(nums)
                nums.pop(nums.index(high))
                hashmap[(low+high)/2.0] = hashmap.get((low+high)/2.0, 0) + 1
            else:
                hashmap[low] = hashmap.get(low, 0) + 1
        return len(hashmap.keys())
        
