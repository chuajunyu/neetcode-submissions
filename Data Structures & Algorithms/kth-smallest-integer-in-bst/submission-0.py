# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, k):            
            left_result = None
            left_weight = 0
            if root.left:
                left_result, left_weight = dfs(root.left, k)
            
            if left_result is not None:
                return left_result, left_weight

            if k - left_weight == 1:
                return root.val, left_weight

            right_result = None
            right_weight = 0
            if root.right:
                right_result, right_weight = dfs(root.right, k - 1 - left_weight)
            
            if right_result is not None:
                return right_result, left_weight + 1 + right_weight

            return None, left_weight + 1 + right_weight
        
        return dfs(root, k)[0]
            


                

            


        