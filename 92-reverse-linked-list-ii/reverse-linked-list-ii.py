# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Treat the starting and ending point as a sublits and then join it together at the end
        # before --> The node preceeding the left one (left -1)
        # tail --> originally left 
        # curr --> the one that we are currently flipping
        # prev
        if not head or left == right:
            return head
        # Phase 1 
        # setup a dummy node
        dummy = ListNode(0,head)
        before = dummy

        for _ in range(left - 1):
            before = before.next

        # Phase 2 
        # do the first flip
        curr = before.next # pasting curr= before.next before is right outside our left
        prev = None # this is becuase i list id completely isolated and hence the prev of the last node needs to be none
        tail = curr
        for i in range (0 , right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        before.next.next = curr
        before.next = prev

        return dummy.next