# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def height(root):
            if root == None:
                return 0
            return max(height(root.left),height(root.right))+1
        
        if root == None:
                return True
        lh = height(root.left)
        rh = height(root.right)

        if (abs(lh-rh) <=1) and self.isBalanced(root.left) and self.isBalanced(root.right) :
            return True

        return False 
        