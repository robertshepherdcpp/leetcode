# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        stack = [[root, [root.val]]]
        count = 0
        while stack:
            node = stack.pop()
            if node[0].left:
                stack.append([node[0].left, node[1]+[node[0].left.val]])
            if node[0].right:
                stack.append([node[0].right, node[1]+[node[0].right.val]])
            if not node[0].left and not node[0].right:
                count += int(''.join(str(i) for i in node[1]), 2)
        return count

        
