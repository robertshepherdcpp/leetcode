# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        dictionary = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            dictionary[node.val] = dictionary.get(node.val, 0) + 1
        value = max(dictionary.values())
        res = []
        for key, val in dictionary.items():
            if value == val:
                res.append(key)
        return res
            
        
