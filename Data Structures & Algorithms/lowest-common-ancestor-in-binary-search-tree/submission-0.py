# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Perform a regular binary search. Once p and q exist on opposite sides of that tree, that node must be the LCA
        if root.val == p.val or root.val == q.val:
            return root

        is_p_left = p.val < root.val
        is_q_left = q.val < root.val

        if is_p_left and is_q_left:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if not is_p_left and not is_q_left:
            return self.lowestCommonAncestor(root.right, p, q)

        return root


        