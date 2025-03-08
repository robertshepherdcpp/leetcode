# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def allValues(root, Left):
            if not root:
                return []
            arr = [root]
            vals = [root.val]
            while arr:
                node = arr.pop()
                if Left:
                    if node.left:
                        arr.append(node.left)
                    if node.right:
                        arr.append(node.right)
                    vals.append(float(node.left.val) if node.left else float('-inf'))
                    vals.append(float(node.right.val) if node.right else float('-inf'))
                else:
                    if node.right:
                        arr.append(node.right)
                    if node.left:
                        arr.append(node.left)
                    vals.append(float(node.right.val) if node.right else float('-inf'))
                    vals.append(float(node.left.val) if node.left else float('-inf'))
            return vals
        print("left:", allValues(root.left, True))
        print("right:", allValues(root.right, False))
        return allValues(root.left, True) == allValues(root.right, False)
        
