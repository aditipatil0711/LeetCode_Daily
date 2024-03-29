# Definition for a binary tree queue.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque([root])
        ans = 0
        while queue:
            ans = queue[0].val
            for _ in range(len(queue)):
                x = queue.popleft()
                if x.left:
                    queue.append(x.left)
                if x.right  :
                    queue.append(x.right)
        return ans


        