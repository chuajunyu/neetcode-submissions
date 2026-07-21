# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Traverse till the end and check if it links to a node that is already visited

        visited = set()

        while head and head.next:
            if head in visited:
                return True
            
            visited.add(head)
            head = head.next
        

        return False
        