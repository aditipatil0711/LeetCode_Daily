# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root,minv,maxv):
            if root is None:
                return True
            if root.val <=minv or root.val >= maxv:
                return False
            left = helper(root.left,minv,root.val)
            right= helper(root.right,root.val,maxv)
            return left and right

        return helper(root,float('-inf'),float('inf'))
        
        