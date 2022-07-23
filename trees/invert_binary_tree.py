class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root: return None 
        leftNode = root.left
        root.left = root.right
        root.right = leftNode

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 