# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1,root))

        depth = 0
        while stack!=[]:
            curr,root = stack.pop()
            if root is not None:
                depth = max(depth, curr)
                stack.append((curr + 1, root.left))
                stack.append((curr + 1, root.right))

        return depth


        