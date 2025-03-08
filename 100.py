# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def allValues(root):
            if not root:
                return []
            arr = [root]
            vals = [root.val]
            while arr:
                node = arr.pop()
                if node.left:
                    arr.append(node.left)
                if node.right:
                    arr.append(node.right)
                vals.append(float(node.left.val) if node.left else float('-inf'))
                vals.append(float(node.right.val) if node.right else float('-inf'))
            return vals
        print("p:", allValues(p))
        print("q:", allValues(q))
        return allValues(p) == allValues(q)
        
