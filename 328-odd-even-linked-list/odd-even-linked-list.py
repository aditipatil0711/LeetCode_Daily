# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next: # Handles empty list and 1 elemt in LL 
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            #Move Odd Pointer
            odd.next = even.next
            odd = odd.next

            #Move Even Pointer
            even.next = odd.next
            even = even.next

        #Attach odd and even lists 
        odd.next = even_head

        return head



        