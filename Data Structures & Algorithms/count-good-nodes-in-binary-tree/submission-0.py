# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_seen=-101):
            if root is None:
                return 0
            
            count = 0
            if root.val >= max_seen:
                count += 1
            
            new_max_seen = max(root.val, max_seen)
            return count + dfs(root.left, new_max_seen) + dfs(root.right, new_max_seen)
        
        return dfs(root)
