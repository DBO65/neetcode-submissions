# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeMap = {}
        curr = head
        size = 0

        while curr:
            nodeMap[size] = curr
            curr = curr.next 
            size += 1
    
        if size == 1:
            return 

        if n == 1:
            nodeMap[size - n - 1].next = None
        elif n == size:
            nodeMap[0].next = None
            head = nodeMap[1]
        else:
            nodeMap[size - n - 1].next = nodeMap[size - n + 1] 

        return head
        

        
