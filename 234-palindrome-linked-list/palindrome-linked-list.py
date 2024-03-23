# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            # alter the direction and find mid
            slow.next, prev, slow= prev, slow, slow.next
        if fast:  # odd number of nodes, slow is the only mid; otherwise it is even
            slow = slow.next
        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True