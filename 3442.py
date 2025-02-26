class Solution(object):
    def maxDifference(self, s):
        dictionary = {}
        for i in s:
            dictionary[i] = 1 + dictionary.get(i, 0)
        highest_odd, lowest_even = float('-inf'), float('inf')
        for i in dictionary.values():
            if i % 2 == 0:
                lowest_even = min(lowest_even, i)
            elif i % 2 == 1:
                highest_odd = max(highest_odd, i)
        return highest_odd-lowest_even
