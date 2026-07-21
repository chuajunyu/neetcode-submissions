# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterate through, always keep a pointer to the merged list

        # Dummy first node
        merged = ListNode(0, None)
        p = merged

        while list1 and list2:
            # compare the values
            if list1.val <= list2.val:
                curr = list1
                list1 = list1.next
                curr.next = None
                p.next = curr
            else:
                curr = list2
                list2 = list2.next
                curr.next = None
                p.next = curr
            
            p = p.next

        if list1:
            p.next = list1
        
        if list2:
            p.next = list2
        
        return merged.next

        