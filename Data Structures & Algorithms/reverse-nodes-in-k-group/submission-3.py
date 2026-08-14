# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # count length of the list
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length += 1

        reverse_times = length // k

        prev = None  # This stores the prev node processed
        curr = head
        counter = 0
        prev_tail = None  # Stores prev tail
        next_tail = None  # Stores next tail
        new_head = None

        while reverse_times > 0:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

            # The first element to be reversed is the tail
            if counter == 0:
                next_tail = prev

            counter += 1
            if counter == k:
                if new_head is None:
                    new_head = prev
                else:
                    prev_tail.next = prev
                prev_tail = next_tail

                reverse_times -= 1
                prev = None
                first = None
                counter = 0

        if curr and prev_tail:
            prev_tail.next = curr
        return new_head


        
        