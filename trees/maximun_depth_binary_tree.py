from collections import deque

class Solution:
    def maxDepth(self, root) -> int:
        #         if not root: return 0

        #         return max(self.maxDepth(root.left), self.maxDepth(root.right) ) + 1
        queue = deque([[root, 1]])
        maxDepth = 0
        while queue:
            current, depth = queue.popleft()
            if current:
                maxDepth = max(maxDepth, depth)

                queue.append([current.left, depth + 1])
                queue.append([current.right, depth + 1])

        return maxDepth


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
