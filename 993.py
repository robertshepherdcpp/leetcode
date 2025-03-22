# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        val = []
        curr = None
        queue = [[root, 0]]
        while queue:
            curr = queue.pop()
            if curr[0].left:
                queue.append([curr[0].left, curr[1]+1, curr[0]])
            if curr[0].right:
                queue.append([curr[0].right, curr[1]+1, curr[0]])
            if curr[0].val == x or curr[0].val == y:
                if val == []:
                    val = curr
                else:
                    return (val[1] == curr[1]) and (curr[2] != val[2])
        return False
