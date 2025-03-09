class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dictionary = {}
        for i in range(len(nums)):
            dictionary[nums[i]] = dictionary.get(nums[i], []) + [i]
        for key, value in dictionary.items():
            if len(value) >= 2:
                l,r=0,1
                while r < len(value):
                    if abs(value[r]-value[l]) <= k:
                        return True
                    l,r=l+1,r+1
        return False

        
