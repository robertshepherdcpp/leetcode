class Solution(object):
    def uniqueOccurrences(self, arr):
        dictionary = {}
        for i in arr:
            dictionary[i] = 1 + dictionary.get(i, 0)
        return len(list(set(dictionary.values()))) == len(dictionary.values())
        
