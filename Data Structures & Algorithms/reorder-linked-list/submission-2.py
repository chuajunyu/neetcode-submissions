# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        seen = set()
        def helper(start, end):
            if end is None:
                return start
            else:
                start = helper(start, end.next)

                if not start:
                    return None

                if start == end or start.next == end:
                    end.next = None
                    return
                
                tmp = start.next
                start.next = end
                end.next = tmp
                return tmp
                

            
        helper(head, head)
        