# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # O(n) space where n is the integer n
        # O(N) time where N is the length of the linked list

        # iterate through the linked list and store every node in a stack
        stack = []
        p = head
        while p is not None:
            stack.append(p)
            p = p.next

        # pop the stack to get to the nth node
        for _ in range(n):
            node = stack.pop()
        
        prev_node = None
        if stack:
            prev_node = stack.pop()

        # remove the node and return the head
        if prev_node:
            prev_node.next = node.next
            return head
        else:
            return node.next