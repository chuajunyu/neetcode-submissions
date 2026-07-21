# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # figure out how long the linked list is
        if head is None:
            return None
        
        first, second = head, head
        while second:
            first = first.next
            if second.next is not None:
                second = second.next.next
            else:
                second = second.next
                 
        # reverse the second half of the linked list, if odd then second half has less

        p1, p2 = None, first
        while p2:
            tmp = p2.next
            p2.next = p1
            p1, p2 = p2, tmp
        
        # merge
        merged = ListNode(0, None)

        p = merged
        while head and p1:
            tmp1 = head.next
            tmp2 = p1.next
            p.next = head
            p.next.next = p1
            p = p1
            head, p1 = tmp1, tmp2
            
        
        if head:
            p.next = head
            p.next.next = None
        return 


        