# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rmdr = 0
        curr1, curr2 = l1, l2
        sol = dummy = ListNode()

        while curr1 and curr2:
            if curr1.val + curr2.val + rmdr <= 9:
                dummy.next = ListNode(curr1.val + curr2.val + rmdr)
                rmdr = 0
                dummy = dummy.next
                curr1, curr2 = curr1.next, curr2.next
            else:
                dummy.next = ListNode(curr1.val + curr2.val + rmdr - 10)
                rmdr = 1 
                dummy = dummy.next
                curr1, curr2 = curr1.next, curr2.next
        
        while curr1:
            if curr1.val + rmdr <= 9:
                dummy.next = ListNode(curr1.val + rmdr)
                rmdr = 0
                dummy = dummy.next
                curr1 = curr1.next
            else:
                dummy.next = ListNode(curr1.val + rmdr - 10)
                rmdr = 1 
                dummy = dummy.next
                curr1 = curr1.next

        while curr2:
            if curr2.val + rmdr <= 9:
                dummy.next = ListNode(curr2.val + rmdr)
                rmdr = 0
                dummy = dummy.next
                curr2 = curr2.next
            else:
                dummy.next = ListNode(curr2.val + rmdr - 10 )
                rmdr = 1 
                dummy = dummy.next
                curr2 = curr2.next
        
        if rmdr == 1:
            dummy.next = ListNode(rmdr)

        
        return sol.next
        

            


        