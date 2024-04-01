# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        stack = []
        if root is not None:
            stack.append((1, root))
        while stack !=[]:
            d,root = stack.pop()
            if root is not None:
                depth = max(depth,d)
                stack.append((d+1,root.left))
                stack.append((d+1, root.right))
        return depth

            