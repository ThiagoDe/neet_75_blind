from threading import currentThread


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current = root
        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right 
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         curr = root

#         while curr:
#             if curr.val < p.val and curr.val < q.val:
#                 # right side
#                 curr = curr.right
#             elif curr.val > p.val and curr.val > q.val:
#                 # left side traverse
#                 curr = curr.left

#             else:
#                 return curr
