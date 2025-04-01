# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        stack = [root]
        all_vals = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            all_vals.append(node.val)
        stack = [root]
        while stack:
            node = stack.pop()
            node.val += sum(filter(lambda x : x > node.val, all_vals))
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
            
        
