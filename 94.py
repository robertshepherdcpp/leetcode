class Solution(object):
    def __init__(self):
        self.arr = []
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            self.arr.append(root.val)
            self.inorderTraversal(root.right)
        return self.arr
