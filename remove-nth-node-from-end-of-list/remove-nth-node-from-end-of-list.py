# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        size = 1
        
        while current != None and current.next != None:
            current = current.next
            size += 1
            
        current = head
                
        if (size - n == 0):
            head = head.next
        else:
            for _ in range(size - n - 1):
                current = current.next
            current.next = current.next.next
        
        
        return head
            
        