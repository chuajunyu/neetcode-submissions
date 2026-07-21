# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        p1, p2 = head, head.next
        head.next = None
        while p2 is not None:
            tmp = p2.next
            p2.next = p1
            p1, p2 = p2, tmp
        return p1

        