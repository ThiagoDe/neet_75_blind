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