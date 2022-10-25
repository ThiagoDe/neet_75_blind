from collections import deque
from collections import deque 

def levelOrder(root):
    queue = deque([root, 0])
    res = []
    while queue:
        node, level = queue.popleft()
        if node:
            if len(res) == level:
                res.append([node.val])
            else:
                res[level].append(node.val)

            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])

    return res 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         res = []

#         queue = deque([(root, 0)])

#         while queue:
#             node, l = queue.popleft()

#             if len(res) == l:
#                 res.append([node.val])
#             else:
#                 res[l].append(node.val)

#             if node.left:
#                 queue.append((node.left, l + 1))

#             if node.right:
#                 queue.append((node.right, l + 1))

#         return res
