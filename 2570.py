class Solution(object):
    def mergeArrays(self, nums1, nums2):
        dictionary = {}
        arr = nums1 + nums2
        for i in arr:
            dictionary[i[0]] = i[1] + dictionary.get(i[0], 0)
        return sorted([list(i) for i in dictionary.items()], key=lambda x: x[0])
        
