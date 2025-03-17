class Solution(object):
    def divideArray(self, nums):
        dictionary = set()
        for i in nums:
            if i in dictionary:
                dictionary.remove(i)
            else:
                dictionary.add(i)
        return len(dictionary) == 0
