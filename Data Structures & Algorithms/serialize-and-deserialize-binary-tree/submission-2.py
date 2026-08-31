# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # bfs
        queue = deque([root])
        result = []
        while queue:
            curr = queue.popleft()
            if curr is None:
                result.append("N")
            else:
                result.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
        return ",".join(result)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        root = None if values[0] == "N" else TreeNode(int(values[0]))
        queue = deque([root])
        index = 1
        while queue:
            curr = queue.popleft()
            if index >= len(values) - 1:
                break
            left_child_val = values[index]
            left_child = None if left_child_val == "N" else TreeNode(int(left_child_val))
            right_child_val = values[index + 1]
            right_child = None if right_child_val == "N" else TreeNode(int(right_child_val))
            curr.left = left_child
            if left_child is not None:
                queue.append(left_child)
            curr.right = right_child
            if right_child is not None:
                queue.append(right_child)
            index += 2
        return root
        



