class Solution(object):
    def isAnagram(self, s, t):
        hm = {}
        for i in s:
            hm[i] = 1 + hm.get(i, 0)
        
        hm2 = {}
        for i in t:
            hm2[i] = 1 + hm2.get(i, 0)
        
        for i in set(hm.keys() + hm2.keys()):
            if i not in hm or i not in hm2 or hm[i] != hm2[i]:
                return False
        return True
        
