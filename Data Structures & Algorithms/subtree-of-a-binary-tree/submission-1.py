# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def isSameTree(self, root, other):
        if root is None and other is None:
            return True
        
        if root and other and root.val == other.val:
            return self.isSameTree(root.left, other.left) and self.isSameTree(root.right, other.right)
        
        return False