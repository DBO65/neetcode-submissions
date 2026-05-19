# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check = set()

        currNode = head
        
        while currNode:
            if currNode in check:
                return True
            check.add(currNode)
            currNode = currNode.next
        return False
        