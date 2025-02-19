class Solution(object):
    def majorityElement(self, nums):
        dictionary = {}
        for i in nums:
            dictionary[i] = 1 + dictionary.get(i, 0)
        count = 0
        for i in dictionary.keys():
            if dictionary.get(i) > len(nums) / 2:
                return i
