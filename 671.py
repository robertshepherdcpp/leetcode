# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        stack = [root]
        smallest = float('inf')
        second_smallest = float('inf')
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if node.val < smallest:
                second_smallest = smallest
                smallest = node.val
            elif node.val < second_smallest and node.val != smallest:
                second_smallest = node.val
        return second_smallest if second_smallest != float('inf') else -1
        
