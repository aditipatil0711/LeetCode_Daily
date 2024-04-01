# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root.left,root.right)

    def check(self,leftroot,rightroot):
        if leftroot is None and rightroot is None:
            return True
        if leftroot is None or rightroot is None:
            return False
        if leftroot.val != rightroot.val:
            return False
        if (leftroot is None and rightroot is None) and (leftroot is not None and rightroot is not None):
            return False
        return self.check(leftroot.left,rightroot.right) and self.check(rightroot.left,leftroot.right)

            
        