# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        stack = [[root, root.val]]
        while stack:
            node = stack.pop()
            if not node[0].left and not node[0].right and node[1] == targetSum:
                return True 
            if node[0].left:
                stack.append([node[0].left, node[1]+node[0].left.val])
            if node[0].right:
                stack.append([node[0].right, node[1]+node[0].right.val])
        return False
        
