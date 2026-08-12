"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # 2 pass
        curr = head
        node_map = {}
        while curr is not None:
            curr_copy = Node(curr.val)
            node_map[curr] = curr_copy
            curr = curr.next

        curr = head
        while curr is not None:
            curr_copy = node_map[curr]
            if curr.next:
                curr_copy.next = node_map[curr.next]
            if curr.random:
                curr_copy.random = node_map[curr.random]
            curr = curr.next

        return node_map[head]
        
        