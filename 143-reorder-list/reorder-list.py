# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        
        l, r = 0, len(arr)-1

        while True:
            node1, node2 = arr[l], arr[r]

            node1_next = node1.next

            if l == r or node1_next == node2:
                node2.next = None
                break

            node1.next = node2
            node2.next = node1_next

            l += 1
            r -= 1

        return