# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        seen = set()
        queue = [root]
        while queue:
            node = queue.pop()
            if (k - node.val) in seen:
                return True
            seen.add(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return False
        
