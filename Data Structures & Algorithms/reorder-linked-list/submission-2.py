# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next
        
        nth = s.next
        prev = s.next = None

        while nth:
            tmp = nth.next 
            nth.next = prev
            prev = nth 
            nth = tmp
        
        nthHead = prev
        curr = head

        while nthHead:
            currSave, nthSave = curr.next, nthHead.next
            curr.next = nthHead
            nthHead.next = currSave

            curr, nthHead = currSave, nthSave


        




            
        