# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.middleNode(head)
        
        secondHalfReversedHead = self.reverseList(middle)
        
        curFirstHalf = head
        curSecondHalf = secondHalfReversedHead
        
        while curFirstHalf and curSecondHalf:
            if curFirstHalf.val != curSecondHalf.val:
                return False
            
            curFirstHalf = curFirstHalf.next
            curSecondHalf = curSecondHalf.next

        return True

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        end = head

        while ((end != None) and (end.next != None)):
            middle = middle.next
            end = end.next.next

        return middle

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        
        while current:
            forward = current.next
            
            current.next = prev
            prev = current
            
            current = forward
        
        return prev