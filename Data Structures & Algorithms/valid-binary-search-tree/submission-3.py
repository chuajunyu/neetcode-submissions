# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            # return whether it's valid, the min node and the max node

            if root is None:
                return True, None, None
            
            is_left_valid, left_min, left_max = helper(root.left)
            is_right_valid, right_min, right_max = helper(root.right)

            if is_left_valid and is_right_valid and (left_max is None or left_max < root.val) and (right_min is None or right_min > root.val):
                # then it's valid
                return True, left_min if left_min is not None else root.val, right_max if right_max is not None else root.val
            
            return False, None, None
        
        return helper(root)[0]
        