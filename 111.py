# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        queue = [[root, 1]]
        min_depth = -1
        while queue:
            vals = queue.pop()
            node = vals[0]
            depth = vals[1]
            if node.left:
                queue.append([node.left, depth+1])
            if node.right:
                queue.append([node.right, depth+1])
            if not node.left and not node.right:
                if min_depth == -1:
                    min_depth = depth
                else:
                    min_depth = min(min_depth, depth)
        return min_depth
        
