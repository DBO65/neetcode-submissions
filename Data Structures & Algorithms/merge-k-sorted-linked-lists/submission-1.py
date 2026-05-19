# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 

        if len(lists) < 2:
            return lists[0]

        ptr1 = lists[0]

        for LL in range(1, len(lists), 1):
            dummy = ListNode()
            head = dummy
            ptr2 = lists[LL]
            
            while ptr1 or ptr2:
                if ptr1 and ptr2:
                    if ptr1.val <= ptr2.val:
                        dummy.next = ptr1
                        ptr1 = ptr1.next
                        dummy = dummy.next
                    else:
                        dummy.next = ptr2
                        ptr2 = ptr2.next
                        dummy = dummy.next
                
                elif ptr1:
                    dummy.next = ptr1
                    ptr1 = ptr1.next
                    dummy = dummy.next
                
                elif ptr2:
                    dummy.next = ptr2
                    ptr2 = ptr2.next
                    dummy = dummy.next

            ptr1 = head.next

        return head.next



        