# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return []
        res = []
        arr = [[root, 0]]
        vals = [[root, 0]]
        max_depth = 1
        while arr:
            val = arr.pop(0)
            node = val[0]
            depth = val[1]
            if node.left:
                arr.append([node.left, depth+1])
                vals.append([node.left, depth+1])
            if node.right:
                arr.append([node.right, depth+1])
                vals.append([node.right, depth+1])
            max_depth = max(max_depth, depth+1)
            print(max_depth)
        for i in range(max_depth):
            res.append([])
        print(res)
        for i in vals:
            res[i[1]].append(i[0].val)
        return res
        




        
