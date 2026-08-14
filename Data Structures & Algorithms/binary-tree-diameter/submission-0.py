# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return 0, 0  # diameter, depth

            left_diameter, left_depth = helper(root.left)
            right_diameter, right_depth = helper(root.right)
            diameter = left_depth + right_depth
            return max(left_diameter, right_diameter, diameter), max(left_depth, right_depth) + 1
        return helper(root)[0]

        