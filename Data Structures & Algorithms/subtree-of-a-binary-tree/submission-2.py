# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # pre-order traversal to serialize both root and subroot
        def serialize(root):
            root_list = []
            q = [root]
            
            while q:
                curr = q.pop()
                if curr:
                    root_list.append(str(curr.val))
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    root_list.append('#')
            return root_list
        
        root_list = serialize(root)
        sub_root_list = serialize(subRoot)

        root_str = "".join(root_list)
        sub_root_str = "".join(sub_root_list)

        return sub_root_str in root_str

        