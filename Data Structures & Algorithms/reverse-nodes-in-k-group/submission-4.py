# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth_node(curr):
            for _ in range(k):
                if curr.next is None:
                    return None
                else:
                    curr = curr.next
            return curr
        
        dummy_head = ListNode(None, head)
        group_prev = dummy_head  # Stores the current group's tail

        while True:
            # Check if there are enough nodes currently
            kth_node = get_kth_node(group_prev)
            if kth_node is None:
                break

            group_next = kth_node.next
            curr, prev = group_prev.next, group_next

            while curr is not group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = group_prev.next
            group_prev.next = kth_node
            group_prev = tmp

        return dummy_head.next