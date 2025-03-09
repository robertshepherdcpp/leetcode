class Solution(object):
    def intersect(self, nums1, nums2):
        ldict = Counter(nums1)
        rdict = Counter(nums2)
        nums = [[i] * min(ldict[i], rdict[i]) for i in set(nums1).intersection(set(nums2))]
        res = []
        for i in nums:
            for j in i:
                res.append(j)
        return res
