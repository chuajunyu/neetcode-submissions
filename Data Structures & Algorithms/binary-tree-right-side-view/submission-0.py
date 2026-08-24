# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS walk of the tree
        # queue that we swap around

        if root is None:
            return []

        q = deque([root])
        next_level = deque()
        result = []
        level = []

        while q:
            curr = q.popleft()
            level.append(curr.val)

            if curr.left:
                next_level.append(curr.left)
            
            if curr.right:
                next_level.append(curr.right)
            
            if not q:
                q, next_level = next_level, q
                result.append(level)
                level = []
        
        return [r[-1] for r in result if r]