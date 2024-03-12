# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(next = head )
        prefix_sum ={}

        curr_sum = 0
        curr_node = dummy
        while curr_node:
            curr_sum += curr_node.val
            prefix_sum[curr_sum] = curr_node
            curr_node = curr_node.next

        curr_sum = 0
        curr_node = dummy
        while curr_node:
            curr_sum += curr_node.val
            curr_node.next = prefix_sum[curr_sum].next
            curr_node = curr_node.next
        return dummy.next       