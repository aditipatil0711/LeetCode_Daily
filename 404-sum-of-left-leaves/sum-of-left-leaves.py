# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum1 = 0
        if root is None:
            return 0
        if root.left and root.left.left is None and root.left.right is None:
            sum1+=root.left.val
        sum1 +=self.sumOfLeftLeaves(root.left)
        sum1 += self.sumOfLeftLeaves(root.right)
        
        return sum1

        