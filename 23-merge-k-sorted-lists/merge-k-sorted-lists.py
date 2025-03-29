# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        heap = []

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap,(l.val,i,l))

        temp = ListNode(0)
        current = temp

        while heap:
            val,i,node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap,(node.next.val, i ,node.next))

        return temp.next
        

        