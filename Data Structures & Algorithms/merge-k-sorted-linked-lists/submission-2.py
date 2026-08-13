# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # insert all into heap

        # convert into a tuple with the priority as the first element
        heap = [(l.val, i, l) for i, l in enumerate(lists)]
        heapq.heapify(heap)
        
        result = ListNode(None)  # Dummy
        curr = result

        while heap:
            _, i, min_node = heapq.heappop(heap)
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, i, min_node.next))
            curr.next = min_node
            min_node.next = None
            curr = curr.next
        
        return result.next

            

        