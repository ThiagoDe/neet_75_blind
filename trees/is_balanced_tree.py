class Solution:
    def isBalanced(self, root) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balenced = (left[0] and right[0] and 
                            abs(left[1] - right[1]) <= 1)
            return [ balenced, 1 + max(left[1], right[1])]

        return dfs(root)[0]