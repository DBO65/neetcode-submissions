# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        s = f = head

        while s and f:
            s = s.next

            if f.next and f.next.next:
                f = f.next.next
            else:
                return False
            if s == f:
                return True


        