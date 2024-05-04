# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node
        next_ = node.next
        while temp:
            temp.val = next_.val
            if next_.next is None:
                break
            temp = temp.next
            next_ = next_.next
        temp.next = None