# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Divide and conquer strategy
        # 1. maxPathSum of the left subtree
        # 2. maxPathSum of the right subtree
        # 3. maxPathSum of a path: left subtree -> root -> right subtree
        # return max(1, 2, 3)
        # how do we get 3?

        def helper(root):
            if root is None:
                return None, 0

            leftmax, left_root_max = helper(root.left)
            rightmax, right_root_max = helper(root.right)
            midmax = root.val
            for x in [left_root_max, right_root_max]:
                if x > 0:
                    midmax += x
            
            maxpath = max([v for v in [leftmax, rightmax, midmax] if v is not None])

            max_root_path = max(left_root_max + root.val, right_root_max + root.val, root.val)
            return maxpath, max_root_path
        
        return helper(root)[0]

