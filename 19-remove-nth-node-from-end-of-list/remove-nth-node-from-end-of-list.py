# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        left = head
        right = head
        for i in range (n):
            right = right.next
        if right == None:
            return head.next
        else:
            while right.next != None :
                right = right.next
                left = left.next
            
            left.next = left.next.next
        return head


        