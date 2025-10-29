# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        def reverse_linked_list(head):
            prev = None
            curr = head
            while curr :
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev


        slow = head
        fast = head

        while fast.next and fast.next.next :
            slow = slow.next 
            fast = fast.next.next
        
        mid = slow 

        next_head = mid.next

        mid.next = None
        second_half_ptr = reverse_linked_list(next_head)
        first_half_ptr  = head
        max_sum = 0

        while second_half_ptr:
            curr_sum = first_half_ptr.val + second_half_ptr.val
            max_sum = max(max_sum, curr_sum)

            first_half_ptr = first_half_ptr.next
            second_half_ptr = second_half_ptr.next
        
        return max_sum 
