# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we just add each node, put it in a new node
        # if there is a carry we record and bring it over
        carry = 0
        result = ListNode(None)  # Dummy node
        curr = result
        while l1 is not None and l2 is not None:
            new_val = l1.val + l2.val + carry
            carry = 0
            if new_val >= 10:
                carry = 1
            new_val = new_val % 10
            curr_node = ListNode(new_val)
            curr.next = curr_node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        # either one or both lists are none
        while l1 is not None:
            new_val = l1.val + carry
            carry = 0
            if new_val >= 10:
                carry = 1
            new_val = new_val % 10
            curr_node = ListNode(new_val)
            curr.next = curr_node
            curr = curr.next
            l1 = l1.next
            
        if l2 is not None:
            new_val = l2.val + carry
            carry = 0
            if new_val >= 10:
                carry = 1
            new_val = new_val % 10
            curr_node = ListNode(new_val)
            curr.next = curr_node
            curr = curr.next
            l2 = l2.next

        if carry == 1:
            curr.next = ListNode(1)

        return result.next

            