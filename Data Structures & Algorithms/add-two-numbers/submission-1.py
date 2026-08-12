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
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            new_val = l1_val + l2_val + carry
            carry = 0
            if new_val >= 10:
                carry = 1
            new_val = new_val % 10
            curr_node = ListNode(new_val)
            curr.next = curr_node
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry == 1:
            curr.next = ListNode(1)

        return result.next

            