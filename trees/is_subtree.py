class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True 
        return (self.isSubtree(root.left, subRoot) or 
                    self.isSubtree(root.right, subRoot))

    def isSameTree(self, r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return (self.isSameTree(r.left, s.left) and
                        self.isSameTree(r.right, s.right))
        return False 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not subRoot:
#             return True

#         if not root:
#             return False

#         if self.sameTree(root, subRoot):
#             return True

#         return (self.isSubtree(root.left, subRoot) or
#                 self.isSubtree(root.right, subRoot))

#     def sameTree(self, s, t):
#         if not s and not t:
#             return True

#         if s and t and s.val == t.val:
#             return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

#         return False
