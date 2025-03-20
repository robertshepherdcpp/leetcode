# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        count = 0
        curr = None
        arr = [root]
        while arr:
            curr = arr.pop()
            if curr.left:
                arr.append(curr.left)
            if curr.right:
                arr.append(curr.right)
            count += 1
        return count
        
