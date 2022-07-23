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
