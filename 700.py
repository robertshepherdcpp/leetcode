# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        arr = []
        while root != None and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left
        return root
        
