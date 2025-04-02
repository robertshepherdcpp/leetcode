# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        stack = [root]
        sum_ = 0
        while stack:
            node = stack.pop()
            if node.val >= low and node.val <= high:
                sum_ += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return sum_

        

        
        
