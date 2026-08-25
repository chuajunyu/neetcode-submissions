# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Use the pre-order traversal array to figure out where in the in-order array to split
        # then based on where the mid is in the in-order array, we know the left and right subtrees for the pre-order too
        # we create the root, then we recurse

        # pre-index what's in the inorder
        in_map = {}
        for i in range(len(inorder)):
            in_map[inorder[i]] = i


        def build(pre_start, pre_end, in_start, in_end):
            if pre_start >= pre_end and in_start >= in_end:
                # There's nothing
                return None
            
            root = TreeNode(preorder[pre_start], None, None)

            i = in_map[preorder[pre_start]]
            
            left_part_len = i - in_start
            right_part_len = in_end - i - 1

            pre_left_start = pre_start + 1
            pre_right_start = pre_left_start + left_part_len
            new_pre_end = pre_right_start + right_part_len

            in_left_end = in_start + left_part_len
            in_right_start = in_left_end + 1
            new_in_end = in_right_start + right_part_len

            root.left = build(pre_left_start, pre_right_start, in_start, in_left_end)
            root.right = build(pre_right_start, new_pre_end, in_right_start, new_in_end)

            return root
        return build(0, len(preorder), 0, len(inorder))

        