# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        length, count = 0, 0 
        counter = head

        while counter:
            counter = counter.next
            length += 1

        target = length - n

        dummy.next = head
        cur = dummy 

        while cur:
            if count == target:
                cur.next = cur.next.next       
            cur = cur.next
            count += 1

        return dummy.next


        
        

        