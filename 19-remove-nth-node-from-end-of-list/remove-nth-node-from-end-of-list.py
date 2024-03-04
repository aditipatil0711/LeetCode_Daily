# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        f,s = head,head
        for i in range(n):
            f = f.next
        if not f:
           return head.next
        while f.next: 
            f,s = f.next,s.next
        s.next = s.next.next
        return head




        