# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        dmax = 1 if root else 0
        depth = 1
        queue = [[root, 1]]
        while queue:
            vals = queue.pop()
            node = vals[0]
            depth = vals[1]
            if node.left: 
                queue.append([node.left, depth+1])
            if node.right: 
                queue.append([node.right,depth+1])
            dmax = max(dmax, depth)
        return dmax
        
