# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        stack = [[root, 0]]
        dictionary = {}
        while stack:
            node = stack.pop()
            dictionary[node[1]] = dictionary.get(node[1], []) + [node[0].val]
            if node[0].left:
                stack.append([node[0].left, node[1]+1])
            if node[0].right:
                stack.append([node[0].right, node[1]+1])
        res = []
        for val in dictionary.values():
            res.append(float(sum(val)/float(len(val))))
        return res
        

        
