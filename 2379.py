class Solution(object):
    def minimumRecolors(self, blocks, k):
        arr = {}
        l,r=0,k
        while r <= len(blocks):
            substr = blocks[l:r]
            arr[substr.count("B")] = substr
            l,r=l+1,r+1
        highest = max(arr.keys())
        return arr[highest].count("W")
        
