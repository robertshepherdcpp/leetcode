# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        stack = [root]
        count = 0
        while stack:
            node = stack.pop()
            if node.left:
                if node.left.left or node.left.right:
                    stack.append(node.left)
                else:
                    count += node.left.val
            if node.right:
                stack.append(node.right)
        return count
        
