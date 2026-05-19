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

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeList(l1,l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, ptr1, ptr2):
        dummy = ListNode()
        head = dummy

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
        return head.next

